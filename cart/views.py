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
            'cost': round(float(games.price),2),
            'qty':1,
            'subtotal' : round(float(games.price),2),
            }
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, "You have added a new game into cart!")
    else:
        messages.success(request, "The game is already in your shopping cart")
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
    
def add_qty(request, cart_id):
    # retrieve the cart from session
    cart = request.session.get('shopping_cart',{})
    
    # if the course is in the cart
    if cart_id in cart:
        # remove it from the cart
        if 'qty' not in cart[cart_id]:
            cart[cart_id]['qty'] = 1
            cart[cart_id]['subtotal'] = round(float(cart[cart_id]['cost']),2),
        else:
            cart[cart_id]['qty'] += 1
            cart[cart_id]['subtotal'] = round(cart[cart_id]['qty'] * float(cart[cart_id]['cost']),2)
        # save back to the session
        request.session['shopping_cart'] = cart
        
    return redirect('/cart/')
    
def remove_qty(request, cart_id):
    # retrieve the cart from session
    cart = request.session.get('shopping_cart',{})
    
    # if the course is in the cart
    if cart_id in cart:
        # remove it from the cart
        if 'qty' not in cart[cart_id]:
            cart[cart_id]['qty'] = 0
        else:
            cart[cart_id]['qty'] -= 1
            cart[cart_id]['subtotal'] = round(cart[cart_id]['qty'] * float(cart[cart_id]['cost']),2)
        # save back to the session
        if cart[cart_id]['qty']<=0:
            del cart[cart_id]
        request.session['shopping_cart'] = cart
        
    return redirect('/cart/')