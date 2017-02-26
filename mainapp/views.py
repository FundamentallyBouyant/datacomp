from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'login.html', {})

def register(request):
    return render(request, 'register.html', {})

def details(request):
    return render(request, 'details.html', {})

def leaderboard(request):
    return render(request, 'leaderboard.html', {})

def contact(request):
    return render(request, 'contact.html', {})