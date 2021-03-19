from django.urls import path
from . import views


urlpatterns = [
    path('', views.load_checkout, name='load_checkout'),
    path('order_confirmation/<order_number>', views.order_confirmation, name='order_confirmation'),
]