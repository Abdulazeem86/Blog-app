from django import forms
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from .models import User, FeedModel

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password1','email']

class FeedForm(forms.ModelForm):
    class Meta:
        model = FeedModel
        fields = ['feed']
=======
from .models import User, PostModel, ProductModel, CategoryModel


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2', 'name','phone']

class PostForm(forms.ModelForm):
    class Meta:
        model=PostModel
        fields = ['feed','image']

class ProductsForm(forms.ModelForm):
    class Meta:
        model= ProductModel
        fields=['prodname','category','price','image','stock','availability']

class CategoryForm(forms.ModelForm):
    class Meta:
        model=CategoryModel
        fields=['choice_text']
>>>>>>> 95c9c8ac83479ad1747c6d8bacb3a1154c4ceaa1
