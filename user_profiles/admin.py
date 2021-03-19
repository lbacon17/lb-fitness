from django.contrib import admin
from .models import StoreUser


class StoreUserAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_email_address',
        'default_phone_number',
        'default_address_line1',
        'default_address_line2',
        'default_town_or_city',
        'default_county_or_region',
        'default_postcode',
        'default_country',
    )

    ordering = ('user',)


admin.site.register(StoreUser, StoreUserAdmin)