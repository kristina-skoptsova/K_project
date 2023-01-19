from django.shortcuts import render
#from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

def index(request):
    return render(request, 'main/index.html')

def profile(request):
    return render(request, 'main/profile.html')

def login(request):
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')

