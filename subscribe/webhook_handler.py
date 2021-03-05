from django.http import HttpResponse
from django.conf import settings

from .models import Package, Subscription
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User

import json
import time


class StripeWH_Handler_Susbcribe:
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
            [subscriber_email]
        )

        def handle_unexpected_event(self, event):
            """Handles an unknown or unexpected webhook event"""
            return HttpResponse(
                content=f'Unexpected webhook received: {event["type"]}',
                status=200)

        def handle_payment_intent_succeeded(self, event):
            """Handles the payment_intent.succeeded webhook from Stripe"""
            intent = event.data.object
            pid = intent.id

            billing_details = intent.charges.data[0].billing_details
            monthly_fee = round(intent.charges.data[0].amount)

            subscription_exists = False
            attempt = 1
            while attempt < 5:
                try subscription = Subscription.objects.get(
                    full_name__iexact=
                )

            self._confirm_subscription_mail()