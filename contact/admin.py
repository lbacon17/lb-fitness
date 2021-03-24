from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'email_address',
        'subject',
        'message',
    )

    ordering = ('user',)

    actions = ['mark_as_answered']

    def mark_as_answered(self, request, queryset):
        queryset.update(answered=True)


admin.site.register(Contact, ContactAdmin)