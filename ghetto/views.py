from django.shortcuts import render
from .models import Postii, Business, Neighborhood, Profile
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def index(request):
    if request.user.profile.neighborhood == None:
        messages.success(request, 'Please fillout you Neighbourhood')
        return redirect('uprofile')
    else:
        neighdetails = Neighborhood.objects.get(
            name=request.user.profile.neighborhood)
        businesses = Business.objects.filter(
            neighborhood=request.user.profile.neighborhood)
        stories = Postii.objects.filter(
            neighborhood=request.user.profile.neighborhood)

        params = {
            'neighdetails': neighdetails,
            'businesses': businesses,
            'stories': stories,
        }
        return render(request, 'index.html', params)

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
