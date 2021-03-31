from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from datetime import timedelta


class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Requests'

    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    answered = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
