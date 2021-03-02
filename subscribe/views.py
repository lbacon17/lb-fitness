from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Package


def subscribe_page(request):
    """This view renders the different subscription packages a user can buy."""
    packages = Package.objects.all()
    context = {
        'packages': packages,
    }
    return render(request, 'subscribe/subscribe.html', context)


@login_required
def get_subscription(request, package_id):
    """This view takes the user to a checkout page where the amount paid depends"""
    """on the subscription plan chosen"""
    package = get_object_or_404(Package, pk=package_id)
    if not request.user.is_authenticated:
        messages.error(request, 'You must create an account to subscribe.')
        return redirect(url, 'account_signup')
    else:
        context = {
            'package': package,
        }
        return render(request, 'subscribe/get_subscription.html', context)
