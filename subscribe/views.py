from django.shortcuts import render, get_object_or_404

from .models import Package


def subscribe_page(request):
    packages = Package.objects.all()
    context = {
        'packages': packages,
    }
    return render(request, 'subscribe/subscribe.html', context)