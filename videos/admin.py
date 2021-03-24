from django.contrib import admin
from .models import Video, Comment


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


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'video',
        'user',
        'content',
        'created_on',
        'approved',
    )

    ordering = ('video',)

    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Video, VideoAdmin)
admin.site.register(Comment, CommentAdmin)