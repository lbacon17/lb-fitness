from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.subscribe_page, name='subscribe_page'),
    path('subscribe/<int:package_id>', views.get_subscription, name='get_subscription'),
]
