from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    return HttpResponse("Welcome to the Social Media API!")
    # Or redirect to another endpoint:
    # return redirect('/posts/')