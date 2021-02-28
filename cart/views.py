from django.shortcuts import render


def load_cart(request):
    """This view render's the user's cart contents"""
    return render(request, 'cart/cart.html')


def add_item(request):
    """This view lets the user add an item to their shopping cart"""
    template = 'cart/cart.html'
    return render(request, template)


def update_cart(request):
    """This view lets the user update their shopping cart"""
    template = 'cart/cart.html'
    return render(request, template)


def remove_item(request):
    """This view lets the user delete an item from their shopping cart"""
    template = 'cart/cart.html'
    return render(request, template)

