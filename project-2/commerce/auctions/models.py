from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Listing(models.Model):
    
    title=models.CharField(max_length=64)
    category=models.CharField(max_length=64,blank=True,null=True)
    price=models.IntegerField()
    imageUrl=models.CharField(max_length=1000,blank=True,null=True)
    activeStatus=models.BooleanField(default=True)
    description=models.CharField(max_length=500)
    owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    watchlist=models.ManyToManyField(User, related_name='myWatchlist',blank=True,null=True)

    def __str__(self):

        return self.title
    
class Comment(models.Model):

    writer=models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    listing=models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comment')
    content=models.CharField(max_length=1000)

    def __str__(self):
        
        return f" In '{self.listing}' '{self.writer}' writes '{self.content}'"
    
class Bid(models.Model):

    bidder=models.ForeignKey(User, on_delete=models.CASCADE, related_name='bid')
    listing=models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bid')
    value=models.IntegerField()

    def __str__(self):
        
        return f" In '{self.listing}' '{self.bidder}' bids '{self.value}'"





    