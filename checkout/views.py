from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import ShopOrderForm
from .models import ShopOrder, OrderLineItem

from shop.models import Product
from user_profiles.models import StoreUser
from user_profiles.forms import StoreUserForm
from cart.contexts import cart_contents

from decimal import Decimal

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_user_info': request.POST.get('save_user_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('There was an issue processing' \
            'your payment. Please try again later.'))
        return HttpResponse(content=e, status=400)


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
            for field in shop_order_form.fields:
                if '  ' in request.POST.get(field):
                    messages.error(request, 'Fields may not contain multiple spaces.')
                    return redirect(reverse('load_checkout'))

            shop_order = shop_order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            shop_order.stripe_pid = pid
            shop_order.shopping_cart = json.dumps(cart)
            shop_order.save()
            for item_id, item_data in cart.items():
                try:
                    item = Product.objects.get(id=item_id)
                    # creates a line item for items without sizes
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            shop_order=shop_order,
                            item=item,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        # creates a line item with sizes
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                shop_order=shop_order,
                                item=item,
                                quantity=quantity,
                                item_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, ('We were unable to locate one '\
                        'of the items in your cart in our database. '\
                        'Please call our customer services team on 01234.'))
                    shop_order.delete()
                    return redirect(reverse('load_cart'))
            request.session['save_user_info'] = 'save-user-info' in request.POST
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
            return redirect(reverse('shop'))
        
        shopping_cart = cart_contents(request)
        total = shopping_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        print(intent)

        if request.user.is_authenticated:
            try:
                user_profile = StoreUser.objects.get(user=request.user)
                shop_order_form = ShopOrderForm(initial={
                    'full_name': user_profile.user.get_full_name(),
                    'email_address': user_profile.user.email,
                    'phone_number': user_profile.default_phone_number,
                    'address_line1': user_profile.default_address_line1,
                    'address_line2': user_profile.default_address_line2,
                    'town_or_city': user_profile.default_town_or_city,
                    'county_or_region': user_profile.default_county_or_region,
                    'postcode': user_profile.default_postcode,
                    'country': user_profile.default_country,
                })
            except StoreUser.DoesNotExist:
                shop_order_form = ShopOrderForm()
        else:
            shop_order_form = ShopOrderForm()
    if not stripe_public_key:
        messages.warning(request, ('Your Stripe public key is missing. Please '\
            'ensure that you have set this in your environment.'))
    
    template = 'checkout/checkout.html'
    context = {
        'shop_order_form': shop_order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def order_confirmation(request, order_number):
    save_user_info = request.session.get('save_user_info')
    shop_order = get_object_or_404(ShopOrder, order_number=order_number)

    if request.user.is_authenticated:
        user_profile = StoreUser.objects.get(user=request.user)
        shop_order.store_user = user_profile
        shop_order.save()

        if save_user_info:
            user_profile_data = {
                'default_email_address': shop_order.email_address,
                'default_phone_number': shop_order.phone_number,
                'default_address_line1': shop_order.address_line1,
                'default_address_line2': shop_order.address_line2,
                'default_town_or_city': shop_order.town_or_city,
                'default_county_or_region': shop_order.county_or_region,
                'default_postcode': shop_order.postcode,
                'default_country': shop_order.country,
            }
            store_user_form = StoreUserForm(user_profile_data,
                                              instance=user_profile)
            if store_user_form.is_valid():
                store_user_form.save()

    messages.success(request, f'Your order has been processed. Your order '\
        f'number is {order_number}. We will send a confirmation e-mail to '\
        f'{shop_order.email_address}.')
    
    if 'cart' in request.session:
        del request.session['cart']
    
    template = 'checkout/order_confirmation.html'
    context = {
        'shop_order': shop_order,
    }

    return render(request, template, context)