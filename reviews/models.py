from django.db import models
from datetime import datetime
from catalog.models import Games


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Reviews(models.Model):
    username = models.CharField(blank=False, max_length=100)
    title = models.ForeignKey(
        Games, on_delete=models.CASCADE,
        null= False,
        blank = False
        )
    rating = IntegerRangeField(null=True, min_value=0, max_value=10)
    # need to limit to ten
    reviews = models.TextField(blank=False)
    posted_on = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = "Reviews"