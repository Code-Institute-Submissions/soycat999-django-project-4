from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import ReviewsForm
from reviews.models import Reviews
from catalog.models import Games
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# View all reviews
def reviews(request):
    all_reviews = Reviews.objects.all()
    return render(request, 'reviews.html',{
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
            messages.success(request, "Reviews for" + " " + newly_created_reviews.title + " has been created!")
    return render(request, 'create_review.html', {
        'form':create_reviews_form
    }) 

@login_required
def delete_reviews(request, reviews_id):
    delete_reviews = get_object_or_404(Reviews, pk=reviews_id)
    return render(request, 'delete_review.html', {
        'reviews':delete_reviews
    })

@login_required
def actually_delete_reviews(request, reviews_id):
    reviews_being_deleted = get_object_or_404(Reviews, pk=reviews_id)
    reviews_being_deleted.delete()
    return redirect(reverse('reviews'))