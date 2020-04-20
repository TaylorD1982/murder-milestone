from django.db import models
from django.utils import timezone


class Review(models.Model):
    """
    A single Review
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField()

    def __unicode__(self):
        return self.title