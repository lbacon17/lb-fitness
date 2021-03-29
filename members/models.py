from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from subscribe.models import Package
from django_countries.fields import CountryField


class Member(models.Model):
    class Meta:
        verbose_name_plural = 'Members'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True, related_name='package')
    default_email_address = models.CharField(max_length=254, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_address_line1 = models.CharField(max_length=80, null=True, blank=True)
    default_address_line2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=50, null=True, blank=True)
    default_county_or_region = models.CharField(max_length=50, null=True, blank=True)
    default_postcode = models.CharField(max_length=10, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    is_vip = models.BooleanField(default=False)

    def set_vip(self):
        self.is_vip = True if self.subscription_package.id == 3 else False
        self.save()

    def __str__(self):
        return self.user.username
