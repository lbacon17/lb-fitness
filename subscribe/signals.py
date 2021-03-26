from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import SubscriptionCount


@receiver(post_save, sender=SubscriptionCount)
def update_on_save(sender, instance, created, **kwargs):
    instance.subscription.update_amount_due()


@receiver(post_delete, sender=SubscriptionCount)
def update_on_delete(sender, instance, **kwargs):
    instance.subscription.update_amount_due()
