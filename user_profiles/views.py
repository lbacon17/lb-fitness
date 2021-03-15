from django.shortcuts import render

from .models import StoreUser


def user_profile(request):
    profile = get_object_or_404(StoreUser, user=request.user)
    template = 'user_profiles/profile.html'
    return render(request, template)