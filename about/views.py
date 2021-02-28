from django.shortcuts import render


def about(request):
    """This view renders the about page"""
    return render(request, 'about/about.html')