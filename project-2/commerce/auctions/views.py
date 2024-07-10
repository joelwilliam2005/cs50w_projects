from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Comment, Bid


def index(request):
    return render(request, "auctions/index.html",{
        'listings':Listing.objects.filter(activeStatus=True)
    })


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

def createListing(request):
    

    if request.method=='POST':

        listing=Listing()

        listing.title=request.POST['title']
        listing.category=request.POST['category']
        listing.price=int(request.POST['price'])
        listing.description=request.POST['description']
        listing.imageUrl=request.POST['imageUrl']
        listing.owner=request.user
        listing.save()
        return HttpResponseRedirect(reverse("index"))


    return render(request, 'auctions/createListing.html')


def listingPage(request, id):

    listing=Listing.objects.get(pk=id)

    if request.user in listing.watchlist.all():

        inWatchlist=True
    
    else:

        inWatchlist=False

    bids=listing.bid.all()
    maxValue=listing.price
    totalBids=0
    isUserHighestBidder=None

    if bids:

        for bid in bids:
            maxValue=max(maxValue,bid.value)

        highestBid=listing.bid.get(value=maxValue)
        
        isUserHighestBidder=request.user==highestBid.bidder

    isOwner=request.user==listing.owner

    isWinner=isUserHighestBidder and listing.activeStatus==False

    return render(request, 'auctions/listingPage.html',{
        'listing':listing,
        'inWatchlist':inWatchlist,
        'comments':Comment.objects.filter(listing=listing),
        'totalBids':len(bids),
        'maxValue':maxValue,
        'isUserHighestBidder':isUserHighestBidder,
        'isOwner':isOwner,
        'isWinner':isWinner,
    })

def categoryPage(request, category):

    listings=Listing.objects.filter(category=category)
    return render(request, "auctions/categoryPage.html",{
        'listings':listings,
        'category':category,
    })

def listCategories(request):

    listings=Listing.objects.all()
    categories=[]

    for listing in listings:

        if listing.category not in categories:

            categories.append(listing.category)

    categories.sort()

    return render(request, 'auctions/listCategories.html',{
        'categories':categories,
    })

def addWatchlist(request, id):

    listing=Listing.objects.get(pk=id)
    listing.watchlist.add(request.user)

    return HttpResponseRedirect(reverse("listingPage", args=(listing.id,)))

def removeWatchlist(request, id):

    listing=Listing.objects.get(pk=id)
    listing.watchlist.remove(request.user)
    
    return HttpResponseRedirect(reverse("listingPage", args=(listing.id,)))

def listWatchlist(request):

    list=request.user.myWatchlist.all()

    return render(request, 'auctions/listWatchlist.html',{
        'list':list,
    })


def addComment(request, id):

    comment=Comment()
    comment.listing=Listing.objects.get(pk=id)
    comment.writer=request.user
    comment.content=request.POST['content']

    comment.save()

    listing=Listing.objects.get(pk=id)
    return HttpResponseRedirect(reverse("listingPage", args=(listing.id,)))
    
def addBid(request, id):

    value=int(request.POST['bidValue'])
    listing=Listing.objects.get(pk=id)
    user=request.user

    if value<listing.price:

        return render(request, 'auctions/bidError.html')

    else:

        bid=Bid()
        bid.listing=listing
        bid.value=value
        bid.bidder=user
        bid.save()

        return HttpResponseRedirect(reverse("listingPage", args=(id,)))
    

def closeAuction(request, id):
    
    listing=Listing.objects.get(pk=id)
    listing.activeStatus=False
    listing.save()

    return HttpResponseRedirect(reverse("listingPage", args=(id,)))

def inActive(request):

    return render(request, "auctions/index.html",{
        'listings':Listing.objects.filter(activeStatus=False)
    })
