from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username

class PostModel(models.Model):
    feed = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post #{self.id}'
    
class FeedModel(models.Model):
    text = models.TextField(max_length=255)

    def __str__(self):
        return self.text

class Group(models.Model):
    # Define your Group model
    pass

class Permission(models.Model):
    # Define your Permission model
    pass