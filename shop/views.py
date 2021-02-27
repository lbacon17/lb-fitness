from django.shortcuts import render

from .models import Product, Category


def shop_all(request):
    """This view renders all items on the main shop page"""
    shop_items = Product.objects.all()
    categories = Category.objects.all()
    query = None
    category = None
    sort = None
    direction = None

    context = {
        'shop_items': shop_items,
        'categories': categories,
    }

    return render(request, 'shop/shop.html', context)