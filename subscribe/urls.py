from django.contrib import admin
from django.urls import path, include
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.subscribe_page, name='subscribe_page'),
    path('subscribe/<int:package_id>', views.get_subscription, name='get_subscription'),
    path('add/<int:package_id>', views.add_package_to_cart, name='add_package_to_cart'),
    path('subscription_confirmation/<subscription_id>', views.subscription_confirmation, name='subscription_confirmation'),
    path('cache_checkout_data', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
