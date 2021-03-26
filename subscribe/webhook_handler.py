from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.models import User

from .models import Package, Subscription
from members.models import Member

import json
import time


class StripeWH_HandlerSubscribe:

    def __init__(self, request):
        self.request = request

    def _confirm_subscription_mail(self):
        subscriber_email = subscription.email_address
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
        subscription_cart = intent.metadata.subscription_cart
        save_member_info = intent.metadata.save_member_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[field] = None
        
        member = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            member = Member.objects.get(user__username=username)
            if save_member_info:
                member.default_email_address = billing_details.email
                member.default_phone_number = shipping_details.phone
                member.default_address_line1 = shipping_details.address.line1
                member.default_address_line2 = shipping_details.address.line2
                member.default_town_or_city = shipping_details.address.city
                member.default_county_or_region = shipping_details.address.state
                member.default_postcode = shipping_details.address.postal_code
                member.default_country = shipping_details.address.country
                member.save()

        subscription_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                subscription = Subscription.objects.get(
                    full_name__iexact=shipping_details.name,
                    email_address__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    cardholder_name__iexact=billing_details.name,
                    address_line1__iexact=shipping_details.address.line1,
                    address_line2__iexact=shipping_details.address.line2,
                    town_or_city__iexact=shipping_details.address.city,
                    county_or_region__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    amount_due=grand_total,
                    active=True,
                    package_in_cart=subscription_cart,
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
                content=f'Webhook received {event["type"]} | SUCCESS: '
                'verified subscription already in database', status=200)
        else:
            subscription = None
            try:
                subscription = Subscription.objects.create(
                    member=member,
                    full_name=shipping_details.name,
                    email_address=billing_details.email,
                    phone_number=shipping_details.phone,
                    cardholder_name=billing_details.name,
                    address_line1=shipping_details.address.line1,
                    address_line2=shipping_details.address.line2,
                    town_or_cityt=shipping_details.address.city,
                    county_or_region=shipping_details.address.state,
                    postcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                    package_in_cart=subscription_cart,
                    active=True,
                    stripe_pid=pid,
                )
                for package_id, package_data in json.loads(subscription_cart.items()):
                    package = Package.objects.get(id=package_id)
                    if isinstance(package_data, int):
                        subscription_count = SubscriptionCount(
                            subscription=subscription,
                            package=package,
                            quantity=package_data,
                        )
                        subscription_count.save()
                    else:
                        subscription.delete()
                        return HttpResponse(
                            content=f'Webhook received: {event["type"]} | ERROR {e}',
                            status=500)
            except Exception as e:
                if subscription:
                    subscription.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} " ERROR: {e}',
                    status=500)
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: '
            f'created subscription in webhook.', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handles the payment_intent.payment_failed webhook"""
        return HttpResponse(
            content=f'Payment failed! Webhook received: {event["type"]}',
            status=200)
