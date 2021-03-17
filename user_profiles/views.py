from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import StoreUser
from .forms import StoreUserForm


def user_profile(request):
    """This view renders the user's profile on their profile page"""
    profile = get_object_or_404(StoreUser, user=request.user)
    """Combine shopuser model with orders to render user order history here"""
    template = 'user_profiles/profile.html'
    return render(request, template)


@login_required
def update_profile(request):
    profile = get_object_or_404(StoreUser, user=request.user)
    if request.method == 'POST':
        form = StoreUserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile information was updated '\
            '   successfully.')
            return redirect(reverse('user_profile'))
        else:
            messages.error(request, 'There was an error submitting your '\
                'information. Please check that you have filled out all '\
                'fields correctly.')
    else:
        form = StoreUserForm(instance=profile)

    template = 'user_profiles/update_profile.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def delete_account(request, user):
    user = request.user
    if request.user != user:
        messages.error(request, 'Sorry, you do not have permission to view '\
            'this page.')
        return redirect(reverse('home'))
    else:
        user.delete()
        messages.success(request, 'Your profile was delete. You will now be '\
            'logged out and redirected to the homepage.')
        return redirect(reverse('home'))