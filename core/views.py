from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def landing(request):
    if request.user.is_authenticated:
        return redirect('dashboard_home')
    return render(request, 'core/landing.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')

        if password != confirm:
            messages.error(request, "Password mile nai")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ei username age theke ache")
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('dashboard_home')

    return render(request, 'core/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard_home')
        else:
            messages.error(request, "Username ba Password vul")
            return redirect('login')

    return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('landing')


@login_required(login_url='login')
def dashboard_home(request):
    return render(request, 'core/dashboard.html')