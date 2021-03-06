from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField (max_length=100, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.subject
