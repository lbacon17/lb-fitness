from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Video
from .forms import VideoForm
from members.models import Member
from django.db.models.functions import Lower


@login_required
def training_videos(request, user):
    """This view renders the videos available to paid subscribers"""
    videos = Video.objects.all()
    member = get_object_or_404(Member, user=user)
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey == 'lower_title'
                videos = videos.annotate(lower_title=Lower('title'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            videos = videos.order_by(sortkey)

    sort_by = f'{sort}_{direction}'

    context = {
        'videos': videos,
        'member': member,
        'sort_by': sort_by,
    }
    return render(request, 'videos/videos.html', context)


@login_required
def add_video(request):
    """This view lets the admin add a new video to the app for"""
    """paid subscribers to view"""
    if request.user.is_superuser:
        if request.method == 'POST':
            form = VideoForm(request.POST, request.FILES)
            if form.is_valid():
                user = request.user
                new_video = form.save()
                messages.success(request, f'Video "{new_video.title}" successfully created.')
                return redirect(reverse('training_videos', args=[user.id]))
            else:
                messages.error(request, 'Sorry, there was an error updating '\
                    'the information. Please ensure all fields are filled '\
                    'out correctly.')
        else:
            form = VideoForm()
    else:
        messages.error(request, 'Sorry, you do not have permission to view this page.')
        return redirect(reverse)
    template = 'videos/add_video.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_video(request, video_id):
    """This view lets the admin make changes to a video in the app"""
    """such as changing its name, description or the file itself"""
    if request.user.is_superuser:
        video = get_object_or_404(Video, pk=video_id)
        if request.method == 'POST':
            form = VideoForm(request.POST, request.FILES, instance=video)
            user = request.user
            if form.is_valid():
                form.save()
                messages.success(request, 'The video information was '\
                    'successfully updated.')
                return redirect(reverse('training_videos', args=[user.id]))
            else:
                messages.error(request, 'Sorry, there was an error updating '\
                    'the information. Please ensure all fields are filled '\
                    'out correctly.')
        else:
            form = VideoForm(instance=video)
    else:
        messages.error(request, 'Sorry, you do not have permission to view this page.')
        return redirect(reverse('home'))

    template = 'videos/edit_video.html'
    context = {
        'form': form,
        'video': video,
    }
    return render(request, template, context)


@login_required
def delete_video(request, video_id):
    """This view lets the admin delete a video from the app"""
    if request.user.is_superuser:
        user = request.user
        video = get_object_or_404(Video, pk=video_id)
        video.delete()
        messages.success(request, f'Successfully deleted "{video.title}" ')
        return redirect(reverse('training_videos', args=[user.id]))
    else:
        messages.error('Sorry, you do not have permission to view this page.')
        return redirect(reverse('home'))