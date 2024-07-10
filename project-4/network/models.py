from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers=models.IntegerField(default=0)
    following=models.IntegerField(default=0)

class Post(models.Model):
    poster=models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content=models.CharField(max_length=1024)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)

    def __str__(self) :
        return f"{self.poster} posted '{self.content}' on {self.timestamp}"

class Follow(models.Model):

    follower=models.ForeignKey(User, on_delete=models.CASCADE, related_name='followerUser')
    following=models.ForeignKey(User, on_delete=models.CASCADE, related_name='followingUser')

    def __str__(self):

        return f"{self.follower} follows {self.following}"
    
class Like(models.Model):

    likerUser=models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')
    likedPost=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')

    def __str__(self):

        return f"{self.likerUser} likes [{self.likedPost}]"