from django.shortcuts import render, redirect, reverse, get_object_or_404
from shop.models import Product


def load_cart(request):
    """This view render's the user's cart contents"""
    return render(request, 'cart/cart.html')


def add_item(request, item_id):
    """This view lets the user add an item to their shopping cart"""
    item = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})
    request.session['cart'] = cart
    return redirect(reverse('shop'))


def update_cart(request):
    """This view lets the user update their shopping cart"""
    template = 'cart/cart.html'
    return render(request, template)


def remove_item(request):
    """This view lets the user delete an item from their shopping cart"""
    template = 'cart/cart.html'
    return render(request, template)

