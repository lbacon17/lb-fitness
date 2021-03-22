from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop_all, name='shop'),
    path('item_info/<item_id>/', views.item_info, name='item_info'),
    path('add_item/', views.add_item, name='add_item'),
    path('edit_item/<item_id>/', views.edit_item, name='edit_item'),
    path('delete_item/<item_id>/', views.delete_item, name='delete_item'),
    path('<item_id>/favourite/', views.favourite_item, name='favourite_item'),
    path('shop_autocomplete', views.shop_autocomplete, name='shop_autocomplete'),
]