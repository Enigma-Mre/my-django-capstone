from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import CustomUserCreationForm

def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('polls:index'))
        else:
            return render(request, 'authentication/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'authentication/login.html')

def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
        })

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('user_auth:login'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})
