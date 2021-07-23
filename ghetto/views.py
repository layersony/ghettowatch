from django.shortcuts import render
from .models import Postii, Business, Neighborhood, Profile
from django.contrib.auth.models import User

def index(request):
  return render(request, 'index.html')

def landing(request):
  return render(request, 'profile/landing.html')

def profile(request):
  return render(request, 'profile/profile.html')

def search(request):
  return render(request, 'search.html')