from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import ShopOrderForm
from .models import ShopOrder

from shop.models import Product
from user_profiles.models import StoreUser
from cart.contexts import cart_contents

import stripe
import json


def load_checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email_address': request.POST['email_address'],
            'phone_number': request.POST['phone_number'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'town_or_city': request.POST['town_or_city'],
            'county_or_region': request.POST['county_or_region'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        shop_order_form = ShopOrderForm(form_data)
        if shop_order_form.is_valid():
            shop_order = shop_order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            shop_order.stripe_pid = pid
            shop_order.shopping_cart = json.dumps(cart)
            shop_order.save()
            for item_id, item_data in cart.items():
                try:
                    item = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            shop_order=shop_order,
                            item=item,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, ('We were unable to locate one '\
                        'of the items in your cart in our database. '\
                        'Please call our customer services team on 01234.'))
                    shop_order.delete()
                    return redirect(reverse('load_cart'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('order_confirmation',
                                     args=[shop_order.order_number]))
        else:
            messages.error(request, ('We were unable to process your order. '\
                                      'Please ensure you have filled out all '\
                                      'fields in the form correctly.'))
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, 'Your cart is currently empty. Please add '\
                            'at lest one item to be able to check out.')
            return redirect(reverse('shop_all'))
        
        shopping_cart = cart_contents(request)
        total = shopping_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )
        if request.user.is_authenticated:
            try:
                store_user_profile = StoreUser.objects.get(user=request.user)
                shop_order_form = ShopOrderForm(initial={
                    'full_name': store_user_profile.user.get_full_name(),
                    'email_address': store_user_profile.user.email,
                    'phone_number': store_user_profile.default_phone_number,
                    'address_line1': store_user_profile.default_address_line1,
                    'address_line2': store_user_profile.default_address_line2,
                    'town_or_city': store_user_profile.default_town_or_city,
                    'county_or_region': store_user_profile.default_county_or_region,
                    'postcode': store_user_profile.default_postcode,
                    'country': store_user_profile.default_country,
                })
            except StoreUser.DoesNotExist:
                shop_order_form = ShopOrderForm()
        else:
            shop_order_form = ShopOrderForm()
    if not stripe_public_key:
        messages.warning(request, ('Your Stripe public key is missing. Please '\
                                    'ensure that you have set this in your '\
                                    'environment.'))
    
    template = 'checkout/checkout.html'
    context = {
        'shop_order_form': shop_order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)