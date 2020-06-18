from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as dj_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

#   Registration new user
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
    return render(request, 'signup.html', {
        'form': form
        
    })
           
#   Profile 
@login_required
def profile(request):
    return render(request, 'profile.html',{
        'current_user':request.user
    })

#   Logout function
@login_required
def logout(request):
    dj_logout(request)
    messages.success(request, "Logged out successfully!")
    return render(request, 'logout.html')



