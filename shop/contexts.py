from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import Product

def favourites():
    """This view iterates through the favourites"""
    favourite_items = []
    shop_items = Product.objects.all()

    for item in shop_items:
        shop_item = get_object_or_404(Product, pk=item_id)
        favourite_items.append(shop_item)

    context = {
        'favourite_items': favourite_items,
    }

    return context
