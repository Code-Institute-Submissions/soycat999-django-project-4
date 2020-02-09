from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    number_of_hours = models.IntegerField(blank=False)
