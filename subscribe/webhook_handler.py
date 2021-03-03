from django.http import HttpResponse
from django.conf import settings

from .models import Package, Subscription
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User

import json
import time


class StripeWH_Handler:
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
