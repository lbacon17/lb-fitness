from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils import timezone

from .forms import SubscriptionForm
from .models import Package, Subscription, SubscriptionCount
from .contexts import subscription_cart

from members.models import Member

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
def add_package_to_cart(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if package_id in list(cart.keys()):
        cart[package_id] += quantity
    else:
        cart[package_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


@login_required
def get_subscription(request, package_id):
    """This view renders the subscription form for the user to fill out"""
    """before completing payment. Credit to ckz870 / Boutique Ado."""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    package = get_object_or_404(Package, pk=package_id)
    if request.method == "POST":
        cart = request.session.get('cart', {})

        billing_info = {
            'full_name': request.POST['full_name'],
            'email_address': request.POST['email_address'],
            'phone_number': request.POST['phone_number'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'town_or_city': request.POST['town_or_city'],
            'county_or_region': request.POST['county_or_region'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        subscription_form = SubscriptionForm(billing_info)
        if subscription_form.is_valid():
            subscription = subscription_form.save(commit=False)
            member = Member.objects.get(user=request.user)
            pid = request.POST.get('client_secret').split('_secret')[0]
            subscription.stripe_pid = pid
            subscription.package_in_cart = json.dumps(cart)
            subscription.save()
            member.subscription_package = package
            member.save()
            for package_id, package_data in cart.items():
                try:
                    package = Package.objects.get(id=package_id)
                    if isinstance(package_data, int):
                        subscription_count = SubscriptionCount(
                            subscription=subscription,
                            package=package,
                            quantity=package_data,
                        )
                        subscription_count.save()
                except Package.DoesNotExist:
                    messages.error(request, 'An error occured.')
                    subscription.delete()
                    return redirect(reverse('get_subscription'))

            request.session['save_member_info'] = 'save-member-info' in request.POST
            return redirect(reverse('subscription_confirmation',
                                     args=[subscription.subscription_id]))
        else:
            messages.error(request, 'There was an error submitting the form.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "You didn't select a subscription")
            return redirect(reverse('subscribe_page'))

        current_cart = subscription_cart(request)
        amount_due = current_cart['amount_due']
        stripe_total = round(amount_due * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        try:
            member = Member.objects.get(user=request.user)
            subscription_form = SubscriptionForm(initial={
                'full_name': member.user.get_full_name(),
                'email_address': member.default_email_address,
                'phone_number': member.default_phone_number,
                'address_line1': member.default_address_line1,
                'address_line2': member.default_address_line2,
                'town_or_city': member.default_town_or_city,
                'county_or_region': member.default_county_or_region,
                'postcode': member.default_postcode,
                'country': member.default_country,
            })
        except Member.DoesNotExist:
            subscription_form = SubscriptionForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe Public Key missing')

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
    save_member_info = request.session.get('save_member_info')
    subscription = get_object_or_404(Subscription, subscription_id=subscription_id)
    member = Member.objects.get(user=request.user)
    subscription.member = member
    subscription.save()

    if save_member_info:
        member_data = {
            'subscription_package': subscription.subscription_package,
            'default_email_address': subscription.email_address,
            'default_phone_number': subscription.phone_number,
            'default_address_line1': subscription.address_line1,
            'default_address_line2': subscription.address_line2,
            'default_town_or_city': subscription.town_or_city,
            'default_county_or_region': subscription.county_or_region,
            'default_postcode': subscription.postcode,
            'default_country': subscription.country,
        }
        membership_form = MembershipForm(member_data, instance=member)
        if membership_form.is_valid():
            membership_form.save()

    messages.success(request, f'Your request was processed successfully. \
        Your subscription ID is {subscription_id}. A confirmation e-mail \
        will be sent to {subscription.email_address}.')

    template = 'subscribe/subscription_confirmation.html'
    context = {
        'subscription': subscription,
        'member': member,
    }

    return render(request, template, context)
