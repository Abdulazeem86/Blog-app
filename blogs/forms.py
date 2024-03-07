from django import forms
from .models import User, FeedModel

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'password', 'email', 'phone']

class FeedForm(forms.ModelForm):
    class Meta:
        model = FeedModel
        fields = ['feed']
