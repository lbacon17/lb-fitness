from django.contrib import admin
from .models import Package, Subscription


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'monthly_rate',
        'videos_available',
        'unlimited_training_and_meal_plans',
        'all_videos_available',
        'shop_discount',
        'plan_description',
    )

    ordering = ('name',)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'subscription_id',
        'member',
        'package',
        'user',
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
        'amount_due',
        'package_in_cart',
        'stripe_pid',
        'active',
    )

    ordering = ('subscription_id',)


admin.site.register(Package, PackageAdmin)
admin.site.register(Subscription, SubscriptionAdmin)