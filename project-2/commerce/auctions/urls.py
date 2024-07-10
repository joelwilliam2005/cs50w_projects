from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('createLisiting',views.createListing, name='createListing'),
    path('listing/<int:id>', views.listingPage, name='listingPage'),
    path('listing/<str:category>', views.categoryPage, name='categoryPage'),
    path('listCategories', views.listCategories, name='listCategories'),
    path('addWatchlist/<int:id>', views.addWatchlist, name='addWatchlist'),
    path('removeWatchlist/<int:id>', views.removeWatchlist, name='removeWatchlist'),
    path('listWatchlist', views.listWatchlist, name='listWatchlist'),
    path('addComment/<int:id>', views.addComment, name='addComment'),
    path('addBid/<int:id>', views.addBid, name='addBid'),
    path('closeAuction/<int:id>', views.closeAuction, name='closeAuction'),
    path('inActive/', views.inActive, name='inActive'),
]
