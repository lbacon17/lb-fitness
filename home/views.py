from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from members.models import Member
from videos.models import Video


def home(request):
    """This view renders the index or home page"""
    return render(request, 'home/index.html')


@login_required
def user_dashboard(request, username):
    """This view renders the individual user's dashboard when logged in"""
    user = get_object_or_404(User, username=request.user)
    videos = Video.objects.all()
    if user.username != username:
        messages.error(request, "You do not have permission to view " \
            "another user's dashboard.")
        return redirect(reverse('home'))
    template = 'home/dashboard.html'
    context = {
        'videos': videos,
        'username': username,
    }
    return render(request, template, context)