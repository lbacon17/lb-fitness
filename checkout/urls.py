from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.load_checkout, name='load_checkout'),
    path('order_confirmation/<order_number>', views.order_confirmation, name='order_confirmation'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]