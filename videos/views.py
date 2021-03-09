from django.shortcuts import render
from .models import Video


def training_videos(request):
    """This view renders the videos available to paid subscribers"""
    videos = Video.objects.all()
    context = {
        'videos': videos,
    }
    return render(request, 'videos/videos.html', context)
