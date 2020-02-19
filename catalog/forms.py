from django import forms
from .models import Games

from pyuploadcare.dj.forms import ImageField

class GamesForm(forms.ModelForm):
    class Meta:
        model=Games
        fields=('title', 'desc', 'price', 'publisher', 'release_date', 'category', 'image')