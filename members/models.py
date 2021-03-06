from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from subscribe.models import Package


class Member(models.Model):
    class Meta:
        verbose_name_plural = 'Members'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False, default=1)
    subscription_package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True, related_name='package')
    default_email_address = models.CharField(max_length=254, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_address_line1 = models.CharField(max_length=80, null=True, blank=True)
    default_address_line2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=50, null=True, blank=True)
    default_county_or_region = models.CharField(max_length=50, null=True, blank=True)
    default_postcode = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def add_subscription_to_user_profile(sender, instance, created, **kwargs):
    """When a user chooses a subscription, this adds the package"""
    """to the user's profile"""
    if created:
        Member.objects.create(user=instance)
    instance.member.save()
