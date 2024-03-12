from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render,  redirect
from django.http import  HttpResponseRedirect, HttpResponse
from django.contrib import messages

from .models import User, PostModel
from .forms import SignUpForm, PostForm


def signup(request):
    if request.method == 'POST':
        print('post method')
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            print('valid form')
            form.save()
            return HttpResponseRedirect('/login') # Redirect to success page after signup
    else:
        print('method not detected')
        form = SignUpForm()
    return render(request, 'blogs/signup.html', {'form': form})


        
# login method-2
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print(username)
        print(password)
        
        if user is not None:
            login(request, user)
            print('user not none')
            return HttpResponseRedirect('/home')
        else:
            print('user none')
            messages.error(request, 'Invalid username or password.')
            return HttpResponseRedirect('/login')
    else:
        print('back to the start')
        form = AuthenticationForm()
        # If it's a GET request, display the login form
        return render(request, 'blogs/login.html',{'form':form}) 


def feed_input(request):
    feeds= PostModel.objects.all()
    if request.method == 'POST':
        print('post method')
        form = PostForm(request.POST)
        if form.is_valid():
            print('successful post')
            form.save()  # Save the form data to the database
            return render(request, 'blogs/home.html', {'feeds': feeds})
            #return HttpResponseRedirect('/home')  # Redirect to a success page
    else:
        form = PostForm()
        print('post method failed')
    return render(request, 'blogs/home.html', {'form': form, 'feeds':feeds})

# def feeds(request):
#     data = FeedModel.objects.all()
#     users = User.objects.all()
#     return render(request, 'blogs/feeds.html', {'data':data, 'users':users})


# def index(request):
#     return render(request, "blogs/signup.html")