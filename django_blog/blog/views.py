from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def home(request):
    return HttpResponse("Welcome to Pascal's Django Blog!")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
