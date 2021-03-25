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
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_user_info = intent.metadata.save_user_info

        billing_info = intent.charges.data[0].billing_info
        delivery_info = intent.delivery_info
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in delivery_info.address.items():
            if value == '':
                shipping_details.address[field] = None
        
        user_profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            user_profile = StoreUser.objects.get(user__username=username)
            if save_user_info:
                user_profile.default_email_address = billing_info.email_address
                user_profile.default_phone_number = delivery_info.phone_number
                user_profile.default_address_line1 = delivery_info.address_line1
                user_profile.default_address_line2 = delivery_info.address_line2
                user_profile.default_town_or_city = delivery_info.town_or_city
                user_profile.default_county_or_region = delivery_info.county_or_region
                user_profile.default_postcode = delivery_info.postcode
                user_profile.default_country = delivery_info.country
                user_profile.save()
        
        shop_order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                shop_order = ShopOrder.objects.get(
                    full_name__iexact=delivery_info.full_name,
                    email_address__iexact=billing_info.email_address,
                    phone_number__iexact=delivery_info.phone_number,
                    address_line1__iexact=delivery_info.address_line1,
                    address_line2__iexact=delivery_info.address_line2,
                    town_or_city__iexact=delivery_info.town_or_city,
                    county_or_region__iexact=delivery_info.county_or_region,
                    postcode__iexact=delivery_info.postcode,
                    country__iexact=delivery_info.country,
                    grand_total=grand_total,
                    shopping_cart=cart,
                    stripe_pid=pid,
                )
                shop_order_exists = True
                break
            except ShopOrder.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if shop_order_exists:
            self._send_confirmation_email(shop_order)
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                         'Verified order already in database'),
                status=200)
        else:
            shop_order = None
            try:
                shop_order = ShopOrder.objects.create(
                    full_name=delivery_info.name,
                    store_user=user_profile,
                    email_address=billing_info.email_address,
                    phone_number=delivery_info.phone_number,
                    address_line1=delivery_info.address_line1,
                    address_line2=delivery_info.address_line2,
                    town_or_city=delivery_info.town_or_city,
                    county_or_region=delivery_info.county_or_region,
                    postcode=delivery_info.postcode,
                    country=delivery_info.country,
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
                                item_size=item_size,
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
            content(f'Webhook received: {event["type"]} | SUCCESS: '
                     f'Created order in webhook.'),
            status=200)
        
    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
