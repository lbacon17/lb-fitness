from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.core.validators import MaxValueValidator, MinValueValidator


class Video(models.Model):

    class Meta:
        verbose_name_plural = 'Videos'

    premium = models.BooleanField(default=False)
    title = models.CharField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00,
                                 null=True, blank=True,
                                 validators=[MaxValueValidator(5),
                                             MinValueValidator(0)])
    length = models.DurationField(null=False, blank=False,
                                  default=timedelta(minutes=0))
    video_file = models.FileField()

    def __str__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rated_video = models.ForeignKey(Video, on_delete=models.CASCADE,
                                    related_name='ratings')
    rating = models.DecimalField(max_digits=3, decimal_places=2,
                                 default=0.00, null=True, blank=True,
                                 validators=[MaxValueValidator(5),
                                             MinValueValidator(0)])


class Comment(models.Model):

    class Meta:
        verbose_name_plural = 'Comments'

    video = models.ForeignKey(Video, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='comments')
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.SET_NULL)
    content = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.content
