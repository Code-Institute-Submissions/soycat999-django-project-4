from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib import messages
from catalog.models import Games
# Create your views here.


def add_to_cart(request, games_id):
    
    games = get_object_or_404(Games, pk=games_id)
    
    
    cart = request.session.get('shopping_cart', {})
    
    # we check if the games_id is not in the cart. If so, we will add it
    if games_id not in cart:
        games = get_object_or_404(Games, pk=games_id)
        # games is found, let's add it to the cart
        cart[games_id] = {
            'id':games_id,
            'title': games.title,
            'cost': 99
            }
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, "You have added a new game!")
    else:
        messages.success(request, "The course is already in your shopping cart")
    return redirect('/catalog/')
        
def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    return render(request, 'cart/view_cart.template.html', {
        'shopping_cart': cart
    })
    
def remove_from_cart(request, course_id):
    # retrieve the cart from session
    cart = request.session.get('shopping_cart',{})
    
    # if the course is in the cart
    if course_id in cart:
        # remove it from the cart
        del cart[course_id]
        # save back to the session
        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart successfully!")
        
    return redirect('/catalog/')