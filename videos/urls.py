from django.urls import path
from . import views

urlpatterns = [
    path('<user>', views.training_videos, name='training_videos'),
    path('add_video/', views.add_video, name='add_video'),
    path('edit_video/<video_id>/', views.edit_video, name='edit_video'),
    path('delete_video/<video_id>', views.delete_video, name='delete_video'),
    path('search/', views.videos_autocomplete, name='videos_autocomplete'),
    path('rate_video/', views.rate_video, name='rate_video'),
]