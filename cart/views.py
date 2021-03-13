from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from shop.models import Product


def load_cart(request):
    """This view render's the user's cart contents"""
    return render(request, 'cart/cart.html')


def add_item_to_cart(request, item_id):
    """This view lets the user add an item to their shopping cart"""
    item = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 (f'Updated size {size.upper()} of {item.name}' \
                                  f'to {cart[item_id]["items_by_size"][size]}'))
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added {item.name} in {size.upper()}')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added {item.name} in {size.upper()}')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, (f'You now have {cart[item_id]} of' \
                              f'{item.friendly_name} in your cart'))
        else:
            cart[item_id] = quantity
            messages.success(request, (f'{cart[item_id]}x {item.friendly_name}' \
                              f'was added to your cart'))
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request):
    """This view lets the user update their shopping cart"""
    template = 'cart/cart.html'
    return render(request, template)


def remove_item_from_cart(request, item_id):
    """This view lets the user delete an item from their shopping cart"""
    try:
        item = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'{item.name} was deleted from your cart.')
        request.session['cart'] = cart
        return render(request, 'cart/cart.html')

    except Exception as e:
        messages.error(request, f'There was a a problem removing item. {e}')
        return HttpResponse(status=500)
