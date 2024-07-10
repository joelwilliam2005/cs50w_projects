from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('login_and_register', views.login_and_register, name='login_and_register'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('api/return_all_users',views.return_all_users, name='return_all_users'),
    path('api/return_all_contacts', views.return_all_contacts, name='return_all_contacts'),
    path('api/add_contact', views.add_contact, name='add_contact'),
    path('api/send_message', views.send_message, name='send_message'),
    path('api/get_conversation', views.get_conversation, name='get_conversation'),

]