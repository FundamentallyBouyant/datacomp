from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^accounts/login',views.custom_login,name='login'),
	# url(r'^register',views.register, name='register'),
	url(r'^details',views.details, name='details'),
	url(r'^leaderboard',views.leaderboard, name='leaderboard'),
	url(r'^contact',views.contact, name='contact'),
	url(r'^accounts/password/reset/done/$', auth_views.password_reset_done,{'template_name' : 'registration/password_reset_done.html'}, name='password_reset_done'),
]