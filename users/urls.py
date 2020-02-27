from django.urls import path
from .views import signup, profile, reviews, create_reviews,delete_reviews,actually_delete_reviews


urlpatterns = [
    path('signup', signup ),
    path('profile', profile),
    path('reviews', reviews,name='reviews'),
    path('delete_reviews/<reviews_id>',delete_reviews,name='delete_reviews'),
    path('actually_delete_reviews/<reviews_id>',actually_delete_reviews,name='actually_delete_reviews'),
    path('create_reviews', create_reviews),

]