from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username

class FeedModel(models.Model):
    feed = models.CharField(max_length=100)
   
    
    # Add more fields as needed