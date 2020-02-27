from django.urls import path
from .views import signup, profile, reviews, create_reviews


urlpatterns = [
    path('signup', signup ),
    path('profile', profile),
    path('reviews', reviews),
    path('create_reviews', create_reviews),

]