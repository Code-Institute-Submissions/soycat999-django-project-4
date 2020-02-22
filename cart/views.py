from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib import messages
from catalog.models import Games
# Create your views here.


def add_to_cart(request, games_id):
    # attempt to get existing cart from the session using the key "shopping_cart"
    # the second argument will be the default value if 
    # if the key does not exist in the session
    cart = request.session.get('shopping_cart', {})
    
    # we check if the course_id is not in the cart. If so, we will add it
    if games_id not in cart:
        games = get_object_or_404(Games, pk=games_id)
        # course is found, let's add it to the cart
        cart[games_id] = {
            'id':games_id,
            'title': games.title,
            'cost': 99
            }
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        
        messages.success(request, "Games has been added to your cart!")
        return redirect('/catalog/')
    else:
        return redirect('/catalog/')