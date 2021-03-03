from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import SubscriptionForm
from .models import Package

import stripe
import json


def subscribe_page(request):
    """This view renders the different subscription packages a user can buy."""
    packages = Package.objects.all()
    context = {
        'packages': packages,
    }
    return render(request, 'subscribe/subscribe.html', context)


@login_required
def get_subscription(request, package_id):
    """This view renders the subscription form for the user to fill out"""
    """before completing payment. Credit to ckz870 / Boutique Ado."""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    package = get_object_or_404(Package, pk=package_id)
    subscription_form = SubscriptionForm()
    
    monthly_rate = package.monthly_rate
    stripe_total = round(monthly_rate * 100)
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    template = 'subscribe/get_subscription.html'
    context = {
        'package': package,
        'subscription_form': subscription_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)
