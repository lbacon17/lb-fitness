from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Video
from members.models import Member


@login_required
def training_videos(request, user):
    """This view renders the videos available to paid subscribers"""
    videos = Video.objects.all()
    member = get_object_or_404(Member, user=user)
    context = {
        'videos': videos,
        'member': member,
    }
    return render(request, 'videos/videos.html', context)
