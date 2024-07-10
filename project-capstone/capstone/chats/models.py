from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class User(AbstractUser):

    contacts=models.ManyToManyField('self', symmetrical=False, blank=True)

class Message(models.Model):

    sender=models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_message')
    reciever=models.ForeignKey(User, on_delete=models.CASCADE, related_name='recieved_message')
    content=models.CharField(max_length=1000)
    timestamp=models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):

        return f"[{self.sender}] to [{self.reciever}] : [{self.content}] on [{timezone.localtime(self.timestamp).strftime('%H:%M')}]"

