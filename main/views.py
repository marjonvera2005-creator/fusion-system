from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Notification

def welcome(request):
    return render(request, 'main/welcome.html')

def dashboard(request):
    return render(request, 'main/dashboard.html')

def about(request):
    return render(request, 'main/about.html')