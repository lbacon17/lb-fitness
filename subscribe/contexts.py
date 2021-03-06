from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from .models import Package


def subscription_cart(request):
    cart_items = []
    total = 0
    count = 0
    cart = request.session.get('cart'. {})

    for item_id in cart.items():
        package = get_object_or_404(Product, pk=package_id)
        total += package.monthly_rate
        count += 1
        cart_items.append({
            'item_id': item_id,
            'quantity': count,
            'package': package,
        })
    amount_due = total
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'count': count,
        'amount_due': amount_due,
    }

    return context
