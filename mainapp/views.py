from django.shortcuts import render
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect

def custom_login(request,**kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return login(request,**kwargs)

def home(request):
    return render(request, 'home.html', {})

# def login(request):
#     return render(request, 'login.html', {})

# def register(request):
#     return render(request, 'register.html', {})

def details(request):
    return render(request, 'details.html', {})

def leaderboard(request):
    return render(request, 'leaderboard.html', {})

def contact(request):
    return render(request, 'contact.html', {})