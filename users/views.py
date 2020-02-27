from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .forms import ReviewsForm
from .models import Reviews
from django.contrib import messages



# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.template.html', {
        'form': form
        
    })
            
@login_required
def profile(request):
    return render(request, 'users/profile.template.html',{
        'current_user':request.user
    })

def reviews(request):
    all_reviews = Reviews.objects.all()
    return render(request, 'users/reviews.template.html',{
        'all_reviews':all_reviews
    })
    
@login_required
def create_reviews(request):
    create_reviews_form=ReviewsForm()
    if request.method == 'POST':
        create_reviews_form = ReviewsForm(request.POST)
        if create_reviews_form.is_valid():  
            # flash message
            newly_created_reviews = create_reviews_form.save()
            messages.success(request, "Reviews" + newly_created_reviews.title + " has been created!")
    return render(request, 'users/create_reviews.template.html', {
        'form':create_reviews_form
    }) 

@login_required
def delete_reviews(request, reviews_id):
    delete_reviews = get_object_or_404(Reviews, pk=reviews_id)
    return render(request, 'users/delete_reviews.template.html', {
        'reviews':delete_reviews
    })

@login_required
def actually_delete_reviews(request, reviews_id):
    reviews_being_deleted = get_object_or_404(Reviews, pk=reviews_id)
    reviews_being_deleted.delete()
    return redirect(reverse('reviews'))