from django.db import models
from datetime import datetime





# Create your models here.

class Reviews(models.Model):
    username = models.CharField(blank=False, max_length=100)
    game_title = models.CharField(blank=False, max_length=50) 
    # -- need to have a dropdown menu for title of games
    rating = models.DecimalField(null=True, max_digits=10, decimal_places=0)
    # need to limit to ten
    reviews = models.TextField(blank=False)
    posted_on = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = "Reviews"