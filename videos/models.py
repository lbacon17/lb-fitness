from django.db import models
from datetime import timedelta


class Video(models.Model):

    class Meta:
        verbose_name_plural = 'Videos'

    title = models.CharField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, null=True, blank=True)
    length = models.DurationField(null=False, blank=False, default=timedelta(minutes=0))
    video_file = models.FileField()

    def __str__(self):
        return self.title
