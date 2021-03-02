from django.db import models


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
