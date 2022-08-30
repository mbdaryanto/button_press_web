import json
from pathlib import Path
from django.shortcuts import render
from django.http import JsonResponse


MANIFEST_JSON = Path(__file__).parent / 'static' / 'manifest.json'


def index(request):
    return render(request, 'counter/home.html', {
        'lib_js': get_lib_js(),
    })


def counter(request):
    return JsonResponse({ 'counter': 1 })


def increment(request):
    return JsonResponse({ 'counter': 2 })


def get_lib_js() -> str:
    with MANIFEST_JSON.open('rb') as f:
        manifest = json.load(f)
        return manifest["src/main.tsx"]["file"]
