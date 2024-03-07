from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

class User(AbstractUser):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.IntegerField()

    def __str__(self):
        return self.username

