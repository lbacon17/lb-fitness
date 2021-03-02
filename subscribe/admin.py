from django.contrib import admin
from .models import Package


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'monthly_rate',
        'videos_available',
        'unlimited_training_and_meal_plans',
        'chat_support',
        'shop_discount',
        'plan_description',
    )

    ordering = ('name',)


admin.site.register(Package, PackageAdmin)