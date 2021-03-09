from django.contrib import admin
from .models import Member, Subscription


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'subscription_package',
        'default_email_address',
        'default_phone_number',
        'default_address_line1',
        'default_address_line2',
        'default_town_or_city',
        'default_county_or_region',
        'default_postcode',
    )

    ordering = ('user',)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'member',
        'active',
    )

    ordering = ('member',)

admin.site.register(Member, MemberAdmin)
admin.site.register(Subscription, SubscriptionAdmin)