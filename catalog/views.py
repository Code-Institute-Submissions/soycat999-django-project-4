from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Games
from .forms import GamesForm

# Create your views here.
def show_games(request):
    all_games = Games.objects.all()
    return render(request, 'catalog/games.template.html', {
        'all_games':all_games
    })
    
    
    
def create_games(request):
    if request.method == 'POST':
        create_games_form = GamesForm(request.POST)
        if create_games_form.is_valid():  
            # flash message
            newly_created_games = create_games_form.save()
            messages.success(request, "Games" + newly_created_games.title + " has been created!")
            
            return redirect(reverse(show_games))
       
    else:
        create_games_form = GamesForm()
    
    return render(request, 'catalog/create_games.template.html', {
        'form':create_games_form
    })
    
    # --Update--
    
def update_games(request, games_id):
    games_being_updated = get_object_or_404(Games, pk=games_id)
    
    
    if request.method == "POST":
        
      update_games_form = GamesForm(request.POST, instance=games_being_updated)
      if update_games_form.is_valid():
          update_games_form.save()
          return redirect(reverse(show_games))
            
    else:
        update_games_form = GamesForm(instance=games_being_updated)
        
    return render(request, 'catalog/update_games.template.html', {
        'form':update_games_form
    })
    
    # --Delete--
def confirm_delete_games(request, games_id):
    games_being_deleted = get_object_or_404(Games, pk=games_id)
    return render(request, 'catalog/confirm_delete_games.template.html', {
        'games':games_being_deleted
    })
    
def actually_delete_games(request, games_id):
    games_being_deleted = get_object_or_404(Games, pk=games_id)
    games_being_deleted.delete()
    return redirect(reverse('show_games'))