from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

# Home view
def home(request):
    return render(request, 'home.html')

# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Profile view (view and update email)
@login_required
def profile(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            request.user.email = email
            request.user.save()
    return render(request, 'profile.html', {'user': request.user})