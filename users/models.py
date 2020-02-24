from django.db import models



# Create your models here.

class Reviews(models.Model):
    Username = models.CharField(blank=False, max_length=100)
    Rating = models.DecimalField(max_digits=10, decimal_places=0)
    Reviews = models.TextField(blank=False)
