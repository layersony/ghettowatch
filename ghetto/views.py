from django.shortcuts import render, redirect
from .models import Postii, Business, Neighborhood, Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm, BusinessForm, PostiiForm
from django.contrib import messages
from django.http import JsonResponse

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


@login_required(login_url='/accounts/login/')
def profile(request):
    print(request.GET)
    if request.method == 'POST':
        print(request.POST)
        userform = UserForm(request.POST or None, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        businessform = BusinessForm(request.POST)
        postiiform = PostiiForm(request.POST)

        curr_neighbourhood = request.user.profile.neighborhood

        if userform.is_valid and profileform.is_valid():
            userform.save()
            profileform.save()
            messages.success(request, 'Profile updated successfully')

        if businessform.is_valid():
            busi = businessform.save(commit=False)
            busi.username = request.user
            busi.neighborhood = curr_neighbourhood
            busi.save()

        if postiiform.is_valid():
            post = postiiform.save(commit=False)
            post.postuser = request.user
            post.neighborhood = curr_neighbourhood
            post.save()

        return redirect('uprofile')
        
    curr_user = Profile.objects.get(username=request.user)
    userform = UserForm(instance=request.user)
    profileform = ProfileForm(instance=request.user.profile)
    businessform = BusinessForm()
    postiiform = PostiiForm()

    allbusiness = Business.objects.filter(username=request.user)
    stories = Postii.objects.filter(postuser=request.user)

    params = {
        'curr_user': curr_user,
        'userform': userform,
        'profileform': profileform,
        'businessform': businessform,
        'postiiform': postiiform,
        'allbusiness': allbusiness,
        'stories': stories
    }
    return render(request, 'profile/index.html', params)


@login_required(login_url='/accounts/login/')
def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        searchresults = Business.searchbusiness(search_term)
        return render(request, 'search.html', {'searchresults': searchresults, 'search_term': search_term})
    else:
        return redirect('home')

def searchajax(request):
    search_term = request.GET.get('search')
    searchresults = Business.searchbusiness(search_term)
    data = {
        'searchresults':searchresults,
        'search_term':search_term
    }
    return JsonResponse(data)