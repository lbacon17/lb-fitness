from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class StoreUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_email_address = models.EmailField(max_length=254, null=False, blank=False)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_address_line1 = models.CharField(max_length=80, null=True, blank=True)
    default_address_line2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=50, null=True, blank=True)
    default_county_or_region = models.CharField(max_length=50, null=True, blank=True)
    default_postcode = models.CharField(max_length=10, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def create_or_update_store_user_profile(sender, instance, created, **kwargs):
#     # if created:
#     StoreUser.objects.create(user=instance)
#     # instance.storeuser.save()
