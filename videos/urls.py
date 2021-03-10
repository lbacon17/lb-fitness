from django.urls import path
from . import views

urlpatterns = [
    path('<user>', views.training_videos, name='training_videos'),
]