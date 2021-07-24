from django.shortcuts import render
from .models import Postii, Business, Neighborhood, Profile
from django.contrib.auth.models import User

def index(request):
  return render(request, 'index.html')

def landing(request):
  return render(request, 'profile/landing.html')

def profile(request):
  return render(request, 'profile/profile.html')

@login_required(login_url='/accounts/login/')
def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        searchresults = Business.searchbusiness(search_term)
        return render(request, 'search.html', {'searchresults': searchresults, 'search_term': search_term})
    else:
        return redirect('home')
