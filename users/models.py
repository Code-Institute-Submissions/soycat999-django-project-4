from django.db import models
from pyuploadcare.dj.models import ImageField




# Create your models here.

class Reviews(models.Model):
    Username = models.CharField(blank=False, max_length=100)
    Title = models.TextField(blank=False, max_length=255)
    Rating = models.DecimalField(max_digits=10, decimal_places=0)
    Reviews = models.TextField(blank=False)
    Image = ImageField(null=True)


    def __str__(self):
        return self.Username
    class Meta:
        verbose_name_plural = "Reviews"