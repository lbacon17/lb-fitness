import uuid

from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Package(models.Model):
    class Meta:
        verbose_name_plural = 'Packages'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    monthly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    videos_available = models.BooleanField(default=False)
    unlimited_training_and_meal_plans = models.BooleanField(default=False)
    chat_support = models.BooleanField(default=False)
    shop_discount = models.BooleanField(default=False)
    plan_description = models.TextField()

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Subscription(models.Model):
    class Meta:
        verbose_name_plural = 'Subscriptions'
    
    from members.models import Member


    subscription_id = models.CharField(max_length=32, null=False, editable=False)
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True, related_name='subscriptions')
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True)
    full_name = models.CharField(max_length=60, null=False, blank=False)
    email_address = models.CharField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address_line1 = models.CharField(max_length=80, null=False, blank=False)
    address_line2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    county_or_region = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    package_in_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')


    def _generate_subscription_id(self):
        """
        Generates a subscription ID using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Sets subscription ID if not set already
        """
        if not self.subscription_id:
            self.subscription_id = self._generate_subscription_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subscription_id
