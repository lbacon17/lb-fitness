from django.urls import path
from . import views


urlpatterns = [
    path('', views.load_cart, name='load_cart'),
    path('add_item/<int:item_id>', views.add_item_to_cart, name='add_item_to_cart'),
    path('update_cart/<int:item_id>', views.update_cart, name='update_cart'),
    path('remove_item/<int:item_id>', views.remove_item_from_cart, name='remove_item_from_cart'),
]