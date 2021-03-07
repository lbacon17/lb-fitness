from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from .models import Package


def subscription_cart(request):
    cart_items = []
    total = 0
    count = 0
    cart = request.session.get('cart', {})

    for package_id, package_data in cart.items():
        if isinstance(package_data, int):
            package = get_object_or_404(Package, pk=package_id)
            total += package_data * package.monthly_rate
            count += package_data
            cart_items.append({
                'package_id': package_id,
                'quantity': package_data,
                'package': package,
            })
        else:
            package = get_object_or_404(Package, pk=package_id)
            for quantity in package_data.items():
                total += quantity * package.monthly_rate
                count += quantity
                cart_items.append({
                    'package_id': package_id,
                    'quantity': quantity,
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
