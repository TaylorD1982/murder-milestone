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
        ('Spectre in the Ballroom', 'Spectre in the Ballroom'),
        ('The Hunting Party', 'The Hunting Party'),
        ('The Corpse in the Drawing Room', 'The Corpse in the Drawing Room'),
        ('A Time to Kill', 'A Time to Kill'),
        ('The Casino Killing', 'The Casino Killing'),
    )
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    response = models.TextField(default='')
    created_date = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(choices=RATING_CHOICES)
    event = models.CharField(max_length = 50, choices = EVENT_CHOICES, default = 'Spectre in the Ballroom'
        )
    
    

    def __unicode__(self):
        return self.title