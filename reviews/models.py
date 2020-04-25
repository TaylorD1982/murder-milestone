from django.db import models
from django.utils import timezone


class Review(models.Model):
    """
    A single Review
    """
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    
    EVENT_CHOICES = (
        ('1', 'Spectre in the Ballroom'),
        ('2', 'The Hunting Party'),
        ('3', 'The Corpse in the Drawing Room'),
        ('4', 'A Time to Kill'),
        ('5', 'The Casino Killing'),
    )
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(choices=RATING_CHOICES)
    event = models.CharField(max_length = 20, choices = EVENT_CHOICES, default = '1'
        )
    
    

    def __unicode__(self):
        return self.title