from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.subscribe_page, name='subscribe_page'),
]
