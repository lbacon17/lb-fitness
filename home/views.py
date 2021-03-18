from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from members.models import Member
from videos.models import Video


def home(request):
    """This view renders the index or home page"""
    return render(request, 'home/index.html')


@login_required
def user_dashboard(request, user):
    """This view renders the individual user's dashboard when logged in"""
    try:    
        member = get_object_or_404(Member, user=user)
        videos = Video.objects.all()
        template = 'home/dashboard.html'
        context = {
            'videos': videos,
            'member': member,
        }
        return render(request, template, context)
    except Member.DoesNotExist:
        raise Http404('User does not exist')