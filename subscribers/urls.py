from django.urls import path
from . import views

urlpatterns = [
    path('<int:subscriber_id>', views.subscribers, name='subscribers'),
]