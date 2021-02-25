from django.shortcuts import render


"""This view renders the index or home page"""
def home(request):
    return render(request, 'home/index.html')
