from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils import timezone

from .forms import SubscriptionForm
from .models import Package, Subscription
from subscribers.models import Subscriber

import stripe
import json
import datetime


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Please try again later.')
        return HttpResponse(content=e, status=400)


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
    if request.method == "POST":
        billing_info = {
            'full_name': request.POST['full_name'],
            'email_address': request.POST['email_address'],
            'phone_number': request.POST['phone_number'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'town_or_city': request.POST['town_or_city'],
            'county_or_region': request.POST['county_or_region'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country']
        }

        subscription_form = SubscriptionForm(billing_info)
        if subscription_form.is_valid():
            subscription = subscription_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            subscription.stripe_pid = pid
            subscription.save()

            return redirect(reverse('subscription_confirmation',
                                     args=[subscription.subscription_id]))
        else:
            messages.error(request, 'There was an error submitting the form.')
    else:
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
        'subscription_form': subscription_form,
        'package': package,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


@login_required
def subscription_confirmation(request, subscription_id):
    """Confirms a successful subscription once user has submitted the form"""
    subscription = get_object_or_404(Subscription, subscription_id=subscription_id)
    subscription.save()
    
    template = 'subscribe/subscription_confirmation.html'
    context = {
        'subscription': subscription,
    }

    return render(request, template, context)
