from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product


def cart_contents(request):
    """This view calculates the cart's total cost by iterating through its contents"""
    items_in_cart = []
    total = 0
    count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            item = get_object_or_404(Product, pk=item_id)
            total += item_data * item.price
            count += item_data
            items_in_cart.append({
                'item_id': item_id,
                'quantity': item_data,
                'item': item,
            })
        else:
            item = get_object_or_404(Product, pk=item_id)
            total += quantity * item.price
            count += quantity
            items_in_cart.append({
                'item_id': item_id,
                'quantity': quantity,
                'item': item,
            })
    
    context = {
        'items_in_cart': items_in_cart,
        'total': total,
        'count': count,
    }

    return context
