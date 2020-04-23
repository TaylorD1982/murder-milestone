from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    description2 = models.TextField(default='')
    address = models.TextField(default='')
    date = models.DateField(blank=True)
    time = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name