from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from subscribe.models import Package


class Subscriber(models.Model):
    class Meta:
        verbose_name_plural = 'Subscribers'
    
    name = models.CharField(max_length=254, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    subscription_package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True, related_name='package')

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def add_subscription_to_user_profile(sender, instance, created, **kwargs):
    """When a user chooses a subscription, this adds the package"""
    """to the user's profile"""
    instance.subscriber.save()
