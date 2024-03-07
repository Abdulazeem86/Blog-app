from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render,  redirect
from django.http import  HttpResponseRedirect, HttpResponse
from django.contrib import messages

from .models import User
from .forms import UserForm

# def index(request):
#     return render(request, "blogs/signup.html")

def home(request):
    return render(request, "blogs/home.html")

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home') # Redirect to success page after signup
    else:
        form = UserForm()
    return render(request, 'blogs/signup.html', {'form': form})

# def login(request):
#     return render(request, "blogs/login.html")

# login method-1
# def user_login(request):
#     if request.method == 'POST':
#         print('post method succeeded')
#         form = AuthenticationForm(request.POST)

#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
            
#             print(username)
#             print(password)
            
#             if user is not None:
#                 login(request, user)
#                 return HttpResponse("Successful Authentication")
#                 # return HttpResponseRedirect('/home')  # Redirect to home page after login
#             else:
#                 print('Blank user field')
#                 messages.error(request, 'Invalid username or password.')
#                 return HttpResponseRedirect('/login')
#         else:
#             print('invalid username or password1')
#             messages.error(request, 'Invalid username or password.')
#             return HttpResponseRedirect('/login')
#     else:
#         form = AuthenticationForm()
#         # return HttpResponse("Authentication failed")
#         return render(request, 'blogs/login.html', {'form': form})
        
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



