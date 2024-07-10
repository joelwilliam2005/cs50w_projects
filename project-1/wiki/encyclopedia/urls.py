from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("createNewPage/", views.createNewPage, name="createNewPage"),
    path("edit/", views.edit, name="edit"),
    path("save/", views.save, name="save"),
    path("randomPage/", views.randomPage, name="randomPage"),
]
