from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import ShopOrder, OrderLineItem
from products.models import Product
from profiles.models import StoreUser

import json
import time


class StripeWH_Handler:

    def __init__(self, request):
        self.request = request
    
    def _send_confirmation_email(self, shop_order):
        customer_email = shop_order.email_address
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'shop_order': shop_order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'shop_order': shop_order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )
    
    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
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
                user_profile.default_phone_number = shipping_details.phone_number
                user_profile.default_address_line1 = shipping_details.address_line1
                user_profile.default_address_line2 = shipping_details.address_line2
                user_profile.default_town_or_city = shipping_details.town_or_city
                user_profile.default_county_or_region = shipping_details.county_or_region
                user_profile.default_postcode = shipping_details.postcode
                user_profile.default_country = shipping_details.country
        
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                shop_order = ShopOrder.objects.get(
                    full_name__iexact=shipping_details.name,
                    email_address__iexact=billing_details.email_address,
                    phone_number__iexact=shipping_details.phone_number,
                    address_line1__iexact=shipping_details.address_line1,
                    address_line2__iexact=shipping_details.address_line2,
                    town_or_city__iexact=shipping_details.town_or_city,
                    county_or_region__iexact=shipping_details.county_or_region,
                    postcode__iexact=shipping_details.postcode,
                    country__iexact=shipping_details.country,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except ShopOrder.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(shop_order)
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                         'Verified order already in database'),
                status=200)
        else:
            shop_order = None
            try:
                shop_order = ShopOrder.objects.create(
                    full_name=shipping_details.name,
                    email_address=billing_details.email_address,
                    phone_number=shipping_details.phone_number,
                    address_line1=shipping_details.address_line1,
                    address_line2=shipping_details.address_line2,
                    town_or_city=shipping_details.town_or_city,
                    county_or_region=shipping_details.county_or_region,
                    postcode=shipping_details.postcode,
                    country=shipping_details.country,
                    grand_total=grand_total,
                    original_cart=cart,
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
            except Exception as e:
                if shop_order:
                    shop_order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR {e}',
                    status=500)
        self._send_confirmation_email(shop_order)
        return HttpResponse(
            content(f'Webhook received: {event["type"]} | SUCCESS: 
                      Created order in webhook.'),
            status=200)
        
        def handle_payment_intent_payment_failed(self event):
            return HttpResponse(
                content=f'Webhook received: {event["type"]}',
                status=200)