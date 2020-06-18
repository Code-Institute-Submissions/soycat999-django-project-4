from django import forms
from reviews.models import Reviews

from pyuploadcare.dj.forms import ImageField

class ReviewsForm(forms.ModelForm):
    class Meta:
        model=Reviews
        fields=('username', 'title', 'rating', 'reviews', 'posted_on')