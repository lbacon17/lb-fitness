from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'name',
        'description',
        'rating',
        'length',
        'video_file',
    )

    ordering = ('title',)


admin.site.register(Video, VideoAdmin)