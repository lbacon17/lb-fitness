from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils import timezone

from .forms import SubscriptionForm
from .models import Package, Subscription, SubscriptionCount
from .contexts import subscription_cart_contents

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
            'subscription_cart': json.dumps(request.session.get('subscription_cart', {})),
            'save_member_info': request.POST.get('save_member_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('There was an issue processing' \
            'your payment. Please try again later.'))
        return HttpResponse(content=e, status=400)


def subscribe_page(request):
    """This view renders the different subscription packages a user can buy."""
    if request.user.is_authenticated:
        if request.user.member:
            messages.error(request, 'You already have a subscription.')
            return redirect(reverse('home'))
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
    subscription_cart = request.session.get('subscription_cart', {})
    if subscription_cart:
        # This block handles the event that a user selects one
        # subscription packages, then goes back and selects a 
        # different package. Each time the user selects a package
        # the cart is emptied before the new one is added so the
        # user is not charged for multiple subscriptions
        subscription_cart.clear()
        if package_id in list(subscription_cart.keys()):
            subscription_cart[package_id] += quantity
        else:
            subscription_cart[package_id] = quantity
    else:
        if package_id in list(subscription_cart.keys()):
            subscription_cart[package_id] += quantity
        else:
            subscription_cart[package_id] = quantity

    request.session['subscription_cart'] = subscription_cart
    return redirect(reverse('get_subscription', args=[package.id]))


@login_required
def get_subscription(request, package_id):
    """This view renders the subscription form for the user to fill out"""
    """before completing payment. Credit to ckz8780 / Boutique Ado."""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.user.member:
        messages.error(request, 'You already have a subscription.')
        return redirect(reverse('home'))

    package = get_object_or_404(Package, pk=package_id)
    if request.method == "POST":
        subscription_cart = request.session.get('subscription_cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email_address': request.POST['email_address'],
            'phone_number': request.POST['phone_number'],
            'cardholder_name': request.POST['cardholder_name'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'town_or_city': request.POST['town_or_city'],
            'county_or_region': request.POST['county_or_region'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        subscription_form = SubscriptionForm(form_data)
        if subscription_form.is_valid():
            subscription = subscription_form.save(commit=False)
            member = Member.objects.create(user=request.user)
            pid = request.POST.get('client_secret').split('_secret')[0]
            subscription.stripe_pid = pid
            subscription.package_in_cart = json.dumps(subscription_cart)
            subscription.save()
            member.subscription_package = package
            if package.id == 3:
                member.is_vip = True
                member.save()
            member.save()
            for package_id, package_data in subscription_cart.items():
                try:
                    package = Package.objects.get(id=package_id)
                    if isinstance(package_data, int):
                        subscription_count = SubscriptionCount(
                            subscription=subscription,
                            package=package,
                            quantity=package_data,
                        )
                        subscription_count.save()
                    else:
                        # Subscription packages do not have sizes or any other
                        # differentiating data, so package_data should always
                        # return an integer. In the unlikely event that it doesn't
                        # the app throws this error, resets the cart and redirects
                        # the user
                        messages.error(request, 'We were unable to locate '\
                            'the subscription in our database. Please try '\
                            'again later.')
                        subscription.delete()
                        return redirect(reverse('subscribe_page'))
                except Package.DoesNotExist:
                    messages.error(request, 'We were unable to locate '\
                        'the subscription in our database. Please try '\
                        'again later.')
                    subscription.delete()
                    return redirect(reverse('subscribe_page'))

            request.session['save_member_info'] = 'save-member-info' in request.POST
            return redirect(reverse('subscription_confirmation',
                                     args=[subscription.subscription_id]))
        else:
            messages.error(request, 'There was an error submitting the form. Please '\
                'ensure that you have filled out all fields correctly.')
    else:
        subscription_cart = request.session.get('subscription_cart', {})
        if not subscription_cart:
            messages.error(request, "You didn't select a subscription")
            # return redirect(reverse('subscribe_page'))

        current_cart = subscription_cart_contents(request)
        grand_total = current_cart['grand_total']
        stripe_total = round(grand_total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        if request.user.is_authenticated:
            try:
                member = Member.objects.get(user=request.user)
                subscription_form = SubscriptionForm(initial={
                    'full_name': member.user.get_full_name(),
                    'email_address': member.user.email,
                    'phone_number': member.default_phone_number,
                    'cardholder_name': member.user.get_full_name(),
                    'address_line1': member.default_address_line1,
                    'address_line2': member.default_address_line2,
                    'town_or_city': member.default_town_or_city,
                    'county_or_region': member.default_county_or_region,
                    'postcode': member.default_postcode,
                    'country': member.default_country,
                })
            except Member.DoesNotExist:
                subscription_form = SubscriptionForm()
        else:
            messages.error(request, 'You must have an account to get a subscription.')
            return redirect(reverse('home'))

    if not stripe_public_key:
        messages.warning(request, ('Your Stripe public key is missing. Please '\
            'ensure that you have set this in your environment.'))

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
    # fix_bug = Subscription.objects.filter(member=None)
    # fix_bug.update(member=1)

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


@login_required
def cancel_subscription(request, user):
    """This view cancels a user's subscription by detaching its user"""
    member = get_object_or_404(Member, user=request.user)
    member.delete()
    messages.success(request, 'Your subscription was successfully '\
        'cancelled. You will no longer be charged for this package.')
    return redirect(reverse('home'))
