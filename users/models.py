from django.db import models
from datetime import datetime

# Create your models here.

class Users(models.Model):
    Username = models.CharField(blank=False, max_length=100)
    Rating = models.IntegerField(max_digits=10)
    Reviews = models.CharField(blank=False, max_length=255)
