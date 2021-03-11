from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from shop.models import Product


def load_cart(request):
    """This view render's the user's cart contents"""
    return render(request, 'cart/cart.html')


def add_item_to_cart(request, item_id):
    """This view lets the user add an item to their shopping cart"""
    item = get_object_or_404(Product, pk=item_id)
    quantity = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'You now have {cart[item_id]} of {item.friendly_name} in your cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'{cart[item_id]}x {item.friendly_name} was added to your cart')
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request):
    """This view lets the user update their shopping cart"""
    template = 'cart/cart.html'
    return render(request, template)


def remove_item_from_cart(request):
    """This view lets the user delete an item from their shopping cart"""
    template = 'cart/cart.html'
    return render(request, template)

