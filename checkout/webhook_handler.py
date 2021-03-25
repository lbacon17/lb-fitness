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
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[field] = None

        shop_order_exists = False
        try:
            shop_order = ShopOrder.objects.get(
                full_name__iexact=shipping_details.name,
                email_address__iexact=billing_details.email,
                phone_number__iexact=shipping_details.phone,
                address_line1__iexact=shipping_details.line1,
                address_line2__iexact=shipping_details.line2,
                town_or_city__iexact=shipping_details.city,
                county_or_region__iexact=shipping_details.state,
                postcode__iexact=shipping_details.postal_code,
                country__iexact=shipping_details.country,
                grand_total=grand_total,
                shopping_cart=cart,
                stripe_pid=pid,
            )
            shop_order_exists = True
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                    'Verified order already in database'), status=200)
        except ShopOrder.DoesNotExist:
            try:
                shop_order = ShopOrder.objects.create(
                    full_name=shipping_details.name,
                    store_user=user_profile,
                    email_address=billing_details.email,
                    phone_number=shipping_details.phone,
                    address_line1=shipping_details.line1,
                    address_line2=shipping_details.line2,
                    town_or_city=shipping_details.city,
                    county_or_region=shipping_details.state,
                    postcode=shipping_details.postal_code,
                    country=shipping_details.country,
                    shopping_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    item = Proudct.objects.get(id=item_id)
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
