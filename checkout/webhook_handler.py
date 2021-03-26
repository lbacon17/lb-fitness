from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import ShopOrder, OrderLineItem
from shop.models import Product
from user_profiles.models import StoreUser

import json
import time


class StripeWH_Handler:

    def __init__(self, request):
        self.request = request
    
    def _send_confirmation_email(self, shop_order):
        customer_email = shop_order.email_address
        subject = render_to_string(
            'checkout/confirmation_emails/shop_confirmation_subject.txt',
            {'shop_order': shop_order})
        body = render_to_string(
            'checkout/confirmation_emails/shop_confirmation_body.txt',
            {'shop_order': shop_order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email],
            fail_silently=False
        )
    
    def handle_event(self, event):
        """Handles an unknown or unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        """Handles the payment_intent.succeeded webhook from Stripe"""
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_user_info = intent.metadata.save_user_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[field] = None

        user_profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            user_profile = StoreUser.objects.get(user__username=username)
            if save_user_info:
                user_profile.default_email_address = billing_details.email
                user_profile.default_phone_number = shipping_details.phone
                user_profile.default_address_line1 = shipping_details.address.line1
                user_profile.default_address_line2 = shipping_details.address.line2
                user_profile.default_town_or_city = shipping_details.address.city
                user_profile.default_county_or_region = shipping_details.address.state
                user_profile.default_postcode = shipping_details.address.postal_code
                user_profile.default_country = shipping_details.address.country
                user_profile.save()

        shop_order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                shop_order = ShopOrder.objects.get(
                    full_name__iexact=shipping_details.name,
                    email_address__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    address_line1__iexact=shipping_details.address.line1,
                    address_line2__iexact=shipping_details.address.line2,
                    town_or_city__iexact=shipping_details.address.city,
                    county_or_region__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    grand_total=grand_total,
                    shopping_cart=cart,
                    stripe_pid=pid,
                )
                shop_order_exists = True
                break
            except ShopOrder.DoesNotExist:
                attempt +=1
                time.sleep(1)
        
        if shop_order_exists:
            self._send_confirmation_email(shop_order)
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                'Verified order already in database'), status=200)
        else:
            shop_order = None
            try:
                shop_order = ShopOrder.objects.create(
                    full_name=shipping_details.name,
                    store_user=user_profile,
                    email_address=billing_details.email,
                    phone_number=shipping_details.phone,
                    address_line1=shipping_details.address.line1,
                    address_line2=shipping_details.address.line2,
                    town_or_city=shipping_details.address.city,
                    county_or_region=shipping_details.address.state,
                    postcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                    shopping_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    item = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            shop_order=shop_order,
                            item=item,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                shop_order=shop_order,
                                item=item,
                                quantity=quantity,
                                item_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                    if shop_order:
                        shop_order.delete()
                        return HttpResponse(
                            content=f'Webhook received: {event["type"]} | ERROR {e}',
                            status=500)
        print(intent) 
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: '
            f'Created order in webhook.', status=200)
        
    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Payment failed! Webhook received: {event["type"]}',
            status=200)
