from django.urls import path
from .views import signup, profile, reviews


urlpatterns = [
    path('signup', signup ),
    path('profile', profile),
    path('reviews', reviews),

]