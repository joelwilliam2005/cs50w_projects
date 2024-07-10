from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import User, Message
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from django.utils import timezone

# Create your views here.

def index(request):

    if not request.user.is_authenticated:

        return HttpResponseRedirect(reverse('login_and_register'))

    else:

        return render(request, 'chats/index.html')
        
    
def login_and_register(request):

    if request.method=='GET':

        return render(request, 'chats/login_and_register.html')
    
    if request.method=='POST':

        if request.POST['LoginOrRegister']=='Register':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            password=request.POST['password']
            
            if username==None and password==None and username=='' and password=='':
                return render(request, 'chats/login_and_register.html')

            user=User.objects.create_user(username,email=None,password=password)
            
            user.first_name=first_name
            user.last_name=last_name
            user.save()

            login(request,user)
            print(request.POST['LoginOrRegister'])

        else:

            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,email=None,password=password)

            if user is not None:
                login(request, user)
            else:
                return render(request, 'chats/login_and_register.html')

            

        return HttpResponseRedirect(reverse('index'))

def logout_user(request):

    logout(request)

    return HttpResponseRedirect(reverse('login_and_register'))

def return_all_users(request):

    all_user_objects = User.objects.all()
    users_data = [{"id": user.id, "username": user.username, "first_name": user.first_name, "last_name": user.last_name} for user in all_user_objects]
    
    return JsonResponse(users_data, safe=False)

def return_all_contacts(request):

    user=User.objects.get(username=request.user.username)
    all_user_contacts= user.contacts.all()

    users_data = [{"id": user.id, "username": user.username, "first_name": user.first_name, "last_name": user.last_name} for user in all_user_contacts]

    return JsonResponse(users_data, safe=False)


@login_required
@csrf_exempt
def add_contact(request):

    user=User.objects.get(username=request.user)
    all_user_contacts= user.contacts.all()
    
    data=json.loads(request.body)

    try:
        contact_user_username=data.get('contact_user')
        contact_user=User.objects.get(username=contact_user_username)

        if contact_user not in all_user_contacts:

            user.contacts.add(contact_user)
            
            return JsonResponse({'success':True})
        
        elif contact_user in all_user_contacts:

            return JsonResponse({'success':True})
        
        else:

            return JsonResponse({'success':False})
    
    except User.DoesNotExist:

        return JsonResponse({'success':False})

@login_required
@csrf_exempt
def send_message(request):

    data=json.loads(request.body)
    content=data.get('message_content')
    reciever_user=User.objects.get(username=data.get('message_sent_to'))    

    message=Message()
    message.sender=User.objects.get(username=request.user)
    message.reciever=reciever_user
    message.content=content
    message.save()

    all_reciever_user_contacts= reciever_user.contacts.all()

    if request.user not in all_reciever_user_contacts:
        reciever_user.contacts.add(request.user)
    
         
    return JsonResponse({
        'success':True,
        'timestamp':f"{timezone.localtime(message.timestamp).strftime('%H:%M')}"
        })

def get_conversation(request):
    
    sender=request.user
    contact_user_username=request.GET.get('contact_user')
    reciever=User.objects.get(username=contact_user_username)

    sent_messages_objects=Message.objects.filter(sender=sender, reciever=reciever)
    recieved_messages_objects=Message.objects.filter(sender=reciever, reciever=sender)

    temp=list(sent_messages_objects)+list(recieved_messages_objects)
    temp.sort(key=lambda msg:msg.timestamp)

    conversation=[{'sender':message.sender.username, 'content':message.content, 'time':f"{timezone.localtime(message.timestamp).strftime('%H:%M') }"} for message in temp]

    return JsonResponse(conversation, safe=False)