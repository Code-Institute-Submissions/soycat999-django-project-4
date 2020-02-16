from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib import messages
from catalog.models import Course
# Create your views here.


def add_to_cart(request, course_id):
    # attempt to get existing cart from the session using the key "shopping_cart"
    # the second argument will be the default value if 
    # if the key does not exist in the session
    cart = request.session.get('shopping_cart', {})
    
    # we check if the course_id is not in the cart. If so, we will add it
    if course_id not in cart:
        course = get_object_or_404(Course, pk=course_id)
        # course is found, let's add it to the cart
        cart[course_id] = {
            'id':course_id,
            'title': course.title,
            'cost': 99
            }
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        
        messages.success(request, "Course has been added to your cart!")
        return redirect('/catalog/')
    else:
        return redirect('/catalog/')