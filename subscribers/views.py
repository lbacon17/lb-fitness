from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Subscriber


@login_required
def subscribers(request, subscriber_id):
    subscribers = Subscriber.objects.all()
    subscriber = get_object_or_404(Subscriber, pk=subscriber_id)
    context = {
        'subscriber': subscriber,
    }
    return render(request, 'subscribers/subscribers.html', context)
