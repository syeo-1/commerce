from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User
from .models import Listing

def index(request):
    # print(request.user)
    # print(request.user.id)
    return render(request, "auctions/index.html", {
        'listings': Listing.objects.all()
    })

def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    # should also be doing a check to see if the listing is part of the user's watchlist
    # if the listing isn't part of their watchlist, should have a bool which is passed to the template
    # in the template, can then render the remove or add to watchlist button based on that info

    # TODO: need code for when user isn't logged in they can stil check out a listing!!!

    # check if the listing is in the current user's watchlist
    logged_in = request.user.is_authenticated
    if logged_in:
        print(request.user)
        user = User.objects.get(username=request.user)
        print(request)
        print(f'username is {user}')
        in_user_watchlist = False
        user_watchlist = [listing for listing in user.listings.all()]

        if listing in user_watchlist:
            in_user_watchlist = True
        # in_user_watchlist = True
        print(listing)
        print(user_watchlist)
        
        print(f'in listing: {in_user_watchlist}')

        return render(request, 'auctions/listing.html', {
            'listing': listing,
            'in_watchlist': in_user_watchlist,
            'user_logged_in': logged_in
        })
    
    else:
        return render(request, 'auctions/listing.html', {
            'listing': listing,
            'user_logged_in': logged_in
        })


def create_listing(request):
    if request.method == 'GET':
        return render(request, 'auctions/create_listing.html' )
    elif request.method == 'POST':
        new_listing = Listing()
        new_listing.title = request.POST.get('title')
        new_listing.description = request.POST.get('description')
        new_listing.current_price = request.POST.get('current_price')
        new_listing.image_url = request.POST.get('image_url')
        new_listing.category = request.POST.get('category')
        # new_listing.associated_user = request.user
        
        new_listing.save()

        return HttpResponseRedirect(reverse('listing', args=(new_listing.id,)))

def watchlist(request):
    # get the current logged in user
    user = User.objects.get(username=request.user)
    print(request)
    print(f'username is {user}')

    # get all listing associated with the user
    watchlist_listings = [listing for listing in user.listings.all()]

    # return all associated listings
    # return render(request, 'auctions/watchlist.html', {
    #     'watchlist': user.listings.all()
    # })
    return render(request, "auctions/watchlist.html", {
        'listings': watchlist_listings
    })

def add_to_watchlist(request, listing_id):
    # check 1:29:20
    if request.method == 'POST':
        print('teststetsets')
        listing = Listing.objects.get(pk=listing_id)
        user = User.objects.get(username=request.user)
        user.listings.add(listing)
        return HttpResponseRedirect(reverse('listing', args=(listing_id,)))

def remove_from_watchlist(request, listing_id):
    if request.method == 'POST':
        listing = Listing.objects.get(pk=listing_id)
        user = User.objects.get(username=request.user)
        user.listings.remove(listing)
        return HttpResponseRedirect(reverse('listing', args=(listing_id,)))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
