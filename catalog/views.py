from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Games, Category
from .forms import GamesForm

# Create your views here.
def show_games(request):
    all_games = Games.objects.all()
    if 'title' in request.GET:
        all_games = all_games.filter(title=request.GET.get('title'))
        print("title received: ", request.GET.get('title'))
    return render(request, 'game_list.html', {
        'all_games':all_games
    })
    
        # --Create--
def handle_uploaded_file(f):
    with open('static/images/test_update.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
@login_required    
def create_games(request):
    if request.method == 'POST':
        create_games_form = GamesForm(request.POST, request.FILES)
        if create_games_form.is_valid():  
            # flash message
            handle_uploaded_file(request.FILES['image'])
            newly_created_games = create_games_form.save()
            messages.success(request, "Games" + newly_created_games.title + " has been created!")
            
            return redirect(reverse(show_games))
       
    else:
        create_games_form = GamesForm()
    
    return render(request, 'create_game.html', {
        'form':create_games_form
    })
    
    # --Update--

@login_required    
def update_games(request, games_id):
    games_being_updated = get_object_or_404(Games, pk=games_id)
    
    
    if request.method == "POST":
        
      update_games_form = GamesForm(request.POST, request.FILES or None, instance=games_being_updated)
      if update_games_form.is_valid():
          edit = update_games_form.save(commit=False)
          edit.save()
          return redirect(reverse(show_games))
            
    else:
        update_games_form = GamesForm(instance=games_being_updated)
        
    return render(request, 'update_game.html', {
        'form':update_games_form
    })
    
    # --Delete--
    
@login_required
def confirm_delete_games(request, games_id):
    games_being_deleted = get_object_or_404(Games, pk=games_id)
    return render(request, 'confirm_delete_game.html', {
        'games':games_being_deleted
    })
    
@login_required    
def actually_delete_games(request, games_id):
    games_being_deleted = get_object_or_404(Games, pk=games_id)
    games_being_deleted.delete()
    return redirect(reverse('show_games'))
    
def show_category(request):
    all_category = Category.objects.all()
    return render(request, 'catalog.html', {
        'all_category':all_category
    })
