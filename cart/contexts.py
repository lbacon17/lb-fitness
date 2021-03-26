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
            if request.user.is_authenticated and request.user.member.subscription_package and request.user.member.subscription_package.id == 3:
                total += (item_data * item.price) / 2
            else:
                total += item_data * item.price
            count += item_data
            items_in_cart.append({
                'item_id': item_id,
                'quantity': item_data,
                'item': item,
            })
        else:
            item = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                if request.user.is_authenticated and request.user.member.subscription_package and request.user.member.subscription_package.id == 3:
                    total += (quantity * item.price) / 2
                else:
                    total += quantity * item.price
                count += quantity
                items_in_cart.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'item': item,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        # if request.user.is_authenticated and request.user.member.subscription_package and request.user.member.subscription_package.id == 3:
        #     delivery = 0
        #     free_delivery_gap = 0
        # else:
        delivery = Decimal(settings.STANDARD_DELIVERY_CHARGE)
        free_delivery_gap = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_gap = 0

    # if request.user.is_authenticated and request.user.member.subscription_package and request.user.member.subscription_package.id == 3:
    #     grand_total = total
    # else:
    grand_total = delivery + total

    context = {
        'items_in_cart': items_in_cart,
        'total': total,
        'count': count,
        'delivery': delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'free_delivery_gap': free_delivery_gap,
        'grand_total': grand_total,
    }

    return context
