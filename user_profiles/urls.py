from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('delete_account/<user>', views.delete_account, name='delete_account'),
    path('order_history/<order_number>', views.user_order_history, name='user_order_history')
]