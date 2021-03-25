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
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: '
            f'Created order in webhook.', status=200)
        
    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Payment failed! Webhook received: {event["type"]}',
            status=200)
