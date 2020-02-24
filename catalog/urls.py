from django.urls import path
# .views refer to the views.py in the current directory as this file

from .views import show_games,show_category, create_games, update_games, confirm_delete_games, actually_delete_games

urlpatterns = [
    path('', show_games, name='show_games'),
    path('create', create_games),
    path('update/<games_id>', update_games, name='update_games'),
    path('confirm_delete/<games_id>', confirm_delete_games),
    path('actually_delete/<games_id>', actually_delete_games, name='delete_games'),
    path('category', show_category, name='show_category'),
]