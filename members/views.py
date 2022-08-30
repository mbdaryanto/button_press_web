from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse, HttpRequest


def login_user(request: HttpRequest):
    """
    login existing user
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # redirect to home
            return redirect('home')
        else:
            # return an invalid login
            messages.warning(request, 'Error in username or password')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')


def logout_user(request: HttpRequest):
    """
    logout user
    """
    logout(request)
    messages.success(request, 'User has been successfully logged out!')

    return redirect('home')


def register_user(request: HttpRequest):
    """
    register user to database using form
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'User registered succesfully!')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'authenticate/register.html', {
        'form': form,
    })


def fetch_user(request: HttpRequest):
    """
    to fetch the user info using json
    """
    if request.user.is_authenticated:
        return JsonResponse({
            'username': request.user.username,
        })
    else:
        return JsonResponse({
            'detail': 'User not authenticated',
        }, status=403)
