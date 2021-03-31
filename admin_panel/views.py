from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required


@login_required
def admin_panel(request):
    if request.user.is_superuser:
        if request.GET:
            if 'choose' in request.GET:
                add_video = request.GET['add_video'].selected
                add_item = request.GET['add_item'].selected
        return render(request, 'admin_panel/admin_panel.html')
    else:
        messages.error(request, 'Sorry, you do not have permission to view '
                       'this page.')
        return redirect(reverse('home'))
