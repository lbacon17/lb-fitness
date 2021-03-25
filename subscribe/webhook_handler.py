from django.http import HttpResponse
from django.conf import settings

from .models import Package, Subscription
from members.models import Member
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User

import json
import time


class StripeWH_HandlerSubscribe:
    def __init__(self, request):
        self.request = request

    def _confirm_subscription_mail(self):
        subscriber_email = user.email_address
        subject = render_to_string(
            'subscribe/confirmation_emails/subscription_confirmation_subject.txt',
            {'package': package})
        body = render_to_string(
            'subscribe/confirmation_emails/subscription_confirmation_body.txt',
            {'package': package, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [subscriber_email],
            fail_silently=False
        )

    def handle_event(self, event):
        """Handles an unknown or unexpected webhook event"""
        return HttpResponse(
            content=f'Unexpected webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handles the payment_intent.succeeded webhook from Stripe"""
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_member_info = intent.metadata.save_member_info

        member_info = intent.member_info
        billing_info = intent.charges.data[0].billing_info
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in member_info.items():
            if value == '':
                member_info[field] = None
        
        for field, value in billing_info.address.items():
            if value == '':
                billing_info.address[field] = None

        member = None
        username = intent.metadata.username

        if username != 'AnonymousUser':
            member = Member.objects.get(user__username-username)
            if save_member_info:
                member.default_email_address = member_info.email_address
                member.default_phone_number = member_info.phone_number
                member.default_cardholder_name = billing_info.cardholder_name
                member.default_address_line1 = billing_info.address_line1
                member.default_address_line2 = billing_info.address_line2
                member.default_town_or_city = billing_info.town_or_city
                member.default_county_or_region = billing_info.county_or_region
                member.default_postcode = billing_info.postcode
                member.default_country = billing_info.country
                member.save()

        subscription_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                subscription = Subscription.objects.get(
                    full_name__iexact=member_info.full_name,
                    email_address__iexact=member_info.email_address,
                    phone_number__iexact=member_info.phone_number,
                    cardholder_name__iexact=billing_info.cardholder_name,
                    address_line1__iexact=billing_info.address.address_line1,
                    address_line2__iexact=billing_info.address.address_line2,
                    town_or_city__iexact=billing_info.address.town_or_city,
                    county_or_region__iexact=billing_info.address.county_or_region,
                    postcode__iexact=billing_info.address.postcode,
                    country__iexact=billing_info.address.country,
                    amount_due=grand_total,
                    package_in_cart=cart,
                    stripe_pid=pid,
                )
                subscription_exists = True
                break
            except Subscription.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if subscription_exists:
            self._confirm_subscription_mail(subscription)
            return HttpResponse(
                content=(f'Webhook received {event["type"]} | SUCCESS.'),
                status=200)
        else:
            subscription = None
            try:
                subscription = Subscription.objects.create(
                    member=member,
                    full_name=member_info.full_name,
                    email_address=member_info.email_address,
                    phone_number=member_info.phone_number,
                    cardholder_name=billing_info.cardholder_name,
                    address_line1=billing_info.address.address_line1,
                    address_line2=billing_info.address.address_line2,
                    town_or_cityt=billing_info.address.town_or_city,
                    county_or_region=billing_info.address.county_or_region,
                    postcode=billing_info.address.postcode,
                    country=billing_info.address.country,
                    package_in_cart=cart,
                    stripe_pid=pid,
                )
                subscription.save()
            except Exception as e:
                if subscription:
                    subscription.delete()
                return HttpResponse(
                    content=(
                        f'Webhook received: {event["type"]} " ERROR: {e}'
                    ), status=500)
        self._confirm_subscription_mail(subscription)
        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | SUCCESS'),
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handles the payment_intent.payment_failed webhook"""
        return HttpResponse(
            content=f'Payment failed: {event["type"]}', status=200)
