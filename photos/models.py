from django.db import models
from django.utils import timezone


class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __unicode__(self):
        return self.title
