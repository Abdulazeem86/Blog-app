from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username


class Group(models.Model):
    # Define your Group model
    pass

class Permission(models.Model):
    # Define your Permission model
    pass