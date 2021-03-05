from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.subscribe_page, name='subscribe_page'),
    path('subscribe/<int:package_id>', views.get_subscription, name='get_subscription'),
    path('subscription_confirmation/<subscription_id>', views.subscription_confirmation, name='subscription_confirmation'),
]
