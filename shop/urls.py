from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.shop_all, name='shop'),
    path('item_info/<int:item_id>/', views.item_info, name='item_info'),
    path('add_item/', views.add_item, name='add_item'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('favourite_item/<int:item_id>', views.favourite_item, name='favourite_item'),
]