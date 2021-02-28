from django.urls import path
from . import views


urlpatterns = [
    path('', views.load_cart, name='load_cart'),
    path('add_item/<item_id>', views.add_item, name='add_item'),
    path('update_cart/<item_id>', views.update_cart, name='update_cart'),
    path('remove_item/<item_id>', views.remove_item, name='remove_item'),
]