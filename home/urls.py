from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/<username>', views.user_dashboard, name='user_dashboard'),
]
