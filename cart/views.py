from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from shop.models import Product
from members.models import Member


def load_cart(request):
    """This view render's the user's cart contents"""
    return render(request, 'cart/cart.html')


def add_item_to_cart(request, item_id):
    """This view lets the user add an item to their shopping cart"""
    item = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'item_size' in request.POST:
        size = request.POST['item_size']
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
            messages.success(request, f'Added {quantity}x {item.name} '\
                              f'in size {size.upper()}')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, (f'Added {quantity}x '\
                              f'{item.friendly_name} to your cart. You now '\
                              f'have {cart[item_id]} of {item.friendly_name} '\
                              f'in your cart'))
        else:
            cart[item_id] = quantity
            messages.success(request, (f'{cart[item_id]}x {item.friendly_name}' \
                              f'was added to your cart'))
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """This view lets the user update the quantity of an item in their cart"""
    item = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'item_size' in request.POST:
        size = request.POST['item_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 99:
            messages.error(request, ('You cannot add this many units of a product. '\
                'The maximum possible quantity is 99. Please enter a quantity '\
                'within the accepted range.'))
        elif quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {item.name} from size {size.upper()}' \
                f'to size {cart[item_id]["items_by_size"][size]}.')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'Removed {item.name} in size {size.upper()}' \
                f'from your cart.')
    else:
        if quantity > 99:
            messages.error(request, ('You cannot add this many units of a product. '\
                'The maximum possible quantity is 99. Please enter a quantity '\
                'within the accepted range.'))
        elif quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Successfully updated quantity of '\
                f'{item.friendly_name} to {cart[item_id]}.')
        else:
            cart.pop(item_id)
            messages.success(request, f'{item.friendly_name} was removed from your cart.')

    request.session['cart'] = cart
    return redirect(reverse('load_cart'))


def remove_item_from_cart(request, item_id):
    """This view lets the user delete an item from their shopping cart"""
    try:
        item = get_object_or_404(Product, pk=item_id)
        size = None
        if 'item_size' in request.POST:
            size = request.POST['item_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'Removed {item.name} in size {size.upper()}' \
                'from your cart.')
        else:
            cart.pop(item_id)
            messages.success(request, f'{item.friendly_name} was deleted from your cart.')

        request.session['cart'] = cart
        return redirect(reverse('load_cart'))

    except Exception as e:
        messages.error(request, f'There was a a problem removing item. {e}')
        return HttpResponse(status=500)
