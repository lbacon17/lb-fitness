from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Member
from .forms import MembershipForm
from subscribe.models import Package, Subscription


@login_required
def member_profile(request):
    """Shows a member's / subscriber's profile"""
    members = Member.objects.all()
    packages = Package.objects.all()
    template = 'members/member_profile.html'
    context = {
        'members': members,
        'packages': packages,
    }
    return render(request, template)


@login_required
def member_subscriptions(request, package_id):
    member = get_object_or_404(Member, user=request.user)
    packages = Package.objects.all()
    package = get_object_or_404(Package, pk=package_id)
    subscriptions = member.subscriptions.all()

    if request.method == 'POST':
        membership_form = MembershipForm(request.POST, instance=member)
        if membership_form.is_valid():
            membership_form.save()
        else:
            messages.error(request, 'Update failed')
    else:
        form = MembershipForm(instance=member)

    template = 'members/member_profile.html'
    context = {
        'packages': packages,
        'package': package,
    }

    return render(request, template, context)
