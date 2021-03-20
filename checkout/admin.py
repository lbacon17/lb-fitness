from django.contrib import admin
from .models import ShopOrder, OrderLineItem


class ShopOrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'store_user',
        'date',
        'full_name',
        'email_address',
        'phone_number',
        'address_line1',
        'address_line2',
        'town_or_city',
        'county_or_region',
        'postcode',
        'country',
        'delivery_charge',
        'order_total',
        'grand_total',
    )

    ordering = ('order_number',)


admin.site.register(ShopOrder, ShopOrderAdmin)
