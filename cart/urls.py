from django.urls import path

from .views import add_to_cart, view_cart, remove_from_cart,add_qty, remove_qty

urlpatterns = [
    
    path('add/<games_id>', add_to_cart, name='add_to_cart'),
    path('add_qty/<cart_id>', add_qty, name='add_qty'),
    path('remove_qty/<cart_id>', remove_qty, name='remove_qty'),
    path('', view_cart, name='view_cart'),
    path('remove/<game_id>', remove_from_cart, name='remove_from_cart'),
]
