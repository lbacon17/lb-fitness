from django.urls import path
from . import views

urlpatterns = [
    path('', views.training_videos, name='training_videos'),
    path('add_video/', views.add_video, name='add_video'),
    path('video_details/<video_id>', views.video_details,
         name='video_details'),
    path('edit_video/<video_id>/', views.edit_video, name='edit_video'),
    path('delete_video/<video_id>', views.delete_video, name='delete_video'),
    path('search/', views.videos_autocomplete, name='videos_autocomplete'),
    path('rate_video/', views.rate_video, name='rate_video'),
    path('update_comment/<video_id>/<comment_id>', views.update_comment,
         name='update_comment'),
    path('delete_comment/<video_id>/<comment_id>', views.delete_comment,
         name='delete_comment'),
    path('approve_comment/<video_id>/<comment_id>', views.approve_comment,
         name='approve_comment'),
    path('reject_comment/<video_id>/<comment_id>', views.reject_comment,
         name='reject_comment'),
]
