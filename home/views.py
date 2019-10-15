from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView as LogoutView


def home(request):
    return render(request, 'home.html')

def my_logout(request):
    logout(request)
    return redirect('home')