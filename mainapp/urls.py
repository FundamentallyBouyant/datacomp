from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^login',views.login, name='login'),
	url(r'^register',views.register, name='register'),
	url(r'^details',views.details, name='details'),
	url(r'^leaderboard',views.leaderboard, name='leaderboard'),
	url(r'^contact',views.contact, name='contact'),
]