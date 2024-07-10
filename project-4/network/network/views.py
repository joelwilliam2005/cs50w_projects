from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def usernamesList():

    list=[]
    for x in User.objects.all():
        list.append(x.username)

    return list

def index(request):
    list=Post.objects.all().order_by('pk').reverse()

    paginator=Paginator(list, 10)
    pageNumber=request.GET.get('page')

    if request.user.is_authenticated:
        usersLikedPost=[x.likedPost for x in Like.objects.filter(likerUser=request.user)]

        return render(request, "network/index.html",{
            'list':paginator.get_page(pageNumber),
            'usersLikedPost':usersLikedPost
        })
    
    else:
        return render(request, "network/index.html",{
            'list':paginator.get_page(pageNumber),
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
    

def newPost(request):

    if request.method=='POST':

        post=Post()

        post.poster=request.user
        post.content=request.POST['content']
        post.save()

        return HttpResponseRedirect(reverse(index))
        
    else:
        return render(request, 'network/newPost.html')

def profile(request, name):

    if not request.user.is_authenticated:
        return render(request, "network/login.html", {
                "message": "Please Login to view other's profile."
            })

    list=usernamesList()
    user=None
    followed=False
    thisUserFollows=[]
    usersWhoFollowThisUser=[]
    

    for x in Follow.objects.filter(follower=request.user):
        thisUserFollows.append(x.following)
    
    for x in Follow.objects.filter(following=request.user):
            usersWhoFollowThisUser.append(x.following)

    if name in list:
        user=User.objects.get(username=name)
        followed=user in thisUserFollows

    allPosts=Post.objects.filter(poster=user).order_by('pk').reverse()
    userFound=True if user else False

    userOnOwnProfile = request.user.username==name

    thisUserFollowsCount=len(thisUserFollows)
    usersWhoFollowThisUserCount=len(usersWhoFollowThisUser)

    usersLikedPost=[x.likedPost for x in Like.objects.filter(likerUser=request.user)]

    paginatorObject=Paginator(allPosts, 10)
    requestKaPage=request.GET.get('page')

    return render(request, 'network/profile.html',{
        'user':user,
        'userFound':userFound,
        'allPosts':paginatorObject.get_page(requestKaPage),
        'followed':followed,
        'userOnOwnProfile':userOnOwnProfile,
        'thisUserFollowsCount':thisUserFollowsCount,
        'usersWhoFollowThisUserCount':usersWhoFollowThisUserCount,
        'usersLikedPost':usersLikedPost
    })
        
def follow(request, name):

    followObject=Follow()
    followObject.follower=request.user
    followObject.following=User.objects.get(username=name)
    followObject.save()

    return HttpResponseRedirect(reverse("profile", args=(name,)))
    

def unfollow(request, name):

    followObject=Follow.objects.get(follower=request.user, following=User.objects.get(username=name))
    followObject.delete()

    return HttpResponseRedirect(reverse("profile", args=(name,)))
    

def following(request):

    userKiFollowing=[x.following for x in Follow.objects.filter(follower=request.user)]
    saariPosts=Post.objects.all().order_by('pk').reverse()
    list=[x for x in saariPosts if x.poster in userKiFollowing]

    usersLikedPost=[x.likedPost for x in Like.objects.filter(likerUser=request.user)]

    paginatorObject=Paginator(list, 10)
    requestKaPage=request.GET.get('page')

    return render(request, "network/index.html",{
        'list':paginatorObject.get_page(requestKaPage),
        'usersLikedPost':usersLikedPost
    })

@login_required
@csrf_exempt
def savePost(request, id):

    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content', '')

        try:
            post = Post.objects.get(id=id, poster=request.user)
            post.content = content
            post.save()
            return JsonResponse({'success': True})
        except Post.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Post not found or permission denied'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

@login_required
@csrf_exempt
def likePost(request, id):

    if request.method=='POST':
        data=json.loads(request.body)
        content = data.get('content', '')
    
        try:
            post = Post.objects.get(id=id)

            if content=='Like':
                post.likes+=1

                likeObject=Like()
                likeObject.likerUser=request.user
                likeObject.likedPost=Post.objects.get(id=id)
                likeObject.save()
            else:
                unlikeObject=Like.objects.get(likerUser=request.user, likedPost=Post.objects.get(id=id))
                unlikeObject.delete()
                post.likes-=1

            post.save()
            return JsonResponse({'success': True})
    
        except Post.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Post not found or permission denied'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

