import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from shop.models import Product
from members.models import Member
from user_profiles.models import StoreUser
from decimal import Decimal


class ShopOrder(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    store_user = models.ForeignKey(StoreUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='shop_orders')
    date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=60, null=False, blank=False)
    email_address = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address_line1 = models.CharField(max_length=80, null=False, blank=False)
    address_line2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    county_or_region = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    delivery_charge = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    shopping_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_cart_total(self):
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_charge = Decimal(settings.STANDARD_DELIVERY_CHARGE)
        else:
            self.delivery_charge = 0
        self.grand_total = self.order_total + self.delivery_charge
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    shop_order = models.ForeignKey(ShopOrder, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    item = models.ForeignKey(Product, null=False, blank=False, on_delete = models.CASCADE)
    item_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
        null=False, blank=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.item.name} on order {self.shop_order.order_number}'
