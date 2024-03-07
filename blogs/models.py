from django.db import models
import datetime

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.IntegerField()

class FeedModel(models.Model):
    feed = models.CharField(max_length=100)
   
    
    # Add more fields as needed