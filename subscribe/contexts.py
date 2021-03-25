from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from .models import Package


def subscription_cart_contents(request):
    cart_items = []
    total = 0
    count = 0
    subscription_cart = request.session.get('subscription_cart', {})
    print(subscription_cart)

    for package_id, package_data in subscription_cart.items():
        if isinstance(package_data, int):
            package = get_object_or_404(Package, pk=package_id)
            total = package.monthly_rate
            count += 1
            cart_items.append({
                'package_id': package_id,
                'quantity': 1,
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

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'count': count,
        'grand_total': grand_total,
    }

    return context
