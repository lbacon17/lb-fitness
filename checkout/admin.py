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


class OrderLineItemAdmin(admin.ModelAdmin):
    list_display = (
        'shop_order',
        'item',
        'item_size',
        'quantity',
        'lineitem_total',
    )

    ordering = ('shop_order',)


admin.site.register(ShopOrder, ShopOrderAdmin)
admin.site.register(OrderLineItem, OrderLineItemAdmin)
