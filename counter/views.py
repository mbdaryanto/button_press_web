from typing import List, Optional
import json
from datetime import timedelta
from pathlib import Path
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.db import transaction
from django.db.models import F
from django.utils import timezone
from .models import PressCounter, UserPress


MANIFEST_JSON = Path(__file__).parent / 'static' / 'manifest.json'


def index(request: HttpRequest):
    """
    homepage where the counter shows, using React.js for the click
    We do not want to refresh the page after clicking the button, so make sure to
    make use of ajax.
    """
    return render(request, 'counter/home.html', {
        'initialCount': read_press_counter(),
        'lib_js': get_lib_js(),
    })


def counter(request: HttpRequest):
    """
    to read the counter
    """
    return JsonResponse({ 'counter': read_press_counter() })


def increment(request: HttpRequest):
    """
    to increment the counter, returning json with updated counter value
    """
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({
                'detail': 'User must be authenticated first'
            }, status=403)
        user = request.user
        at = timezone.now()
        # A user should only be allowed to press the button 5 times every 60 seconds
        lower_range = at - timedelta(seconds=60)

        with transaction.atomic():
            number_of_presses = UserPress.objects.filter(at__gte=lower_range, user=user).select_for_update().count()
            if number_of_presses >= 5:
                return JsonResponse({ 'detail': 'You may only press the button 5 times or less within 60 seconds'}, status=403)
            user_press = UserPress(
                user=user,
                at=at,
            )
            user_press.save()

            _counter = increment_press_counter()
            return JsonResponse({ 'counter': _counter })

    return JsonResponse({ 'detail': 'Method not allowed'}, status=403)


def get_lib_js() -> str:
    """
    reading .js file from the manifest.json
    """
    with MANIFEST_JSON.open('rb') as f:
        manifest = json.load(f)
        return manifest["src/main.tsx"]["file"]


def read_press_counter() -> int:
    """
    read the press counter from the db
    """
    _counter = get_counter_singleton()

    if _counter is None:
        # if no records found return 0
        return 0

    return _counter.number


def increment_press_counter() -> int:
    """
    increment the counter and return the updated counter value
    """
    _counter = get_counter_singleton()

    if _counter is None:
        new_counter = PressCounter(number=1)
        new_counter.save()
        return new_counter.number

    _counter.number = F('number') + 1
    _counter.save()
    _counter.refresh_from_db()

    return _counter.number


def get_counter_singleton() -> Optional[PressCounter]:
    """
    return Press Counter singleton or None
    """
    press_counters = PressCounter.objects.order_by('id').select_for_update()[:1]

    if len(press_counters) == 0:
        return None

    if len(press_counters) != 1:
        raise ValueError('Press Counter query error')

    return press_counters[0]
