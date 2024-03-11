from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, FeedModel

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password1','email']

class FeedForm(forms.ModelForm):
    class Meta:
        model = FeedModel
        fields = ['feed']
