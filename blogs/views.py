from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, get_user_model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import  HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.views import generic
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import PostModel, FeedModel
from .forms import SignUpForm, PostForm


# def signup(request):
#     if request.method == 'POST':
#         print('post method')
#         form = SignUpForm(request.POST)
        
#         if form.is_valid():
#             print('valid form')
#             form.save()
#             return HttpResponseRedirect('/login') # Redirect to success page after signup
#     else:
#         print('method not detected')
#         form = SignUpForm()
#     return render(request, 'blogs/signup.html', {'form': form})




# #Generic signup
class SignUpView(CreateView):
    model=get_user_model
    template_name="blogs/signup.html"
    form_class=SignUpForm
    success_url=reverse_lazy("blogs:login")

    def form_valid(self, form):
        messages.success(self.request,"account has been created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)

        
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
            return HttpResponseRedirect('/feed')
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
            form.save()  
            return render(request, 'blogs/home.html', {'feeds': feeds})
    else:
        form = PostForm()
        print('post method failed')
    print("render method called")
    return render(request, 'blogs/home.html', {'form': form, 'feeds':feeds})






class FeedView(generic.ListView):
    template_name= "blogs/feed.html"
    context_object_name = "text"

    def get_queryset(self):
        return FeedModel.objects.all()
    




class FeedInputView(CreateView):
    model = PostModel
    form_class = PostForm
    template_name = 'blogs/homegeneric.html'
    success_url = reverse_lazy('blogs:homegeneric') 

    def form_valid(self, form):
        print('successful post')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('post method failed')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs): #Here in the context method works without **kwargs but added as an optional input for future needs)
        context = super().get_context_data(**kwargs) 
        context['feeds'] = PostModel.objects.all().order_by('created_at')[::-1]
        return context
    
    


# class Feed_inputView(generic.CreateView, generic.ListView):
#     model=PostModel
#     form_class=PostForm
#     template_name= "blogs/homegeneric.html"
#     context_object_name = "feeds"

#     def get_queryset(self):
#         return PostModel.objects.all()
    
#     def form_valid(self, form):
#         return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = self.get_form()
    #     return context








    
# #Generic view of feed_input
# class feed_inputView(generic.DetailView):
#     model = PostModel
#     form_class = PostForm
#     template_name = 'blogs/home.html'
#     success_url = reverse('home')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['feeds'] = PostModel.objects.all()
#         return context

# def feeds(request):
#     data = FeedModel.objects.all()
#     users = User.objects.all()
#     return render(request, 'blogs/feeds.html', {'data':data, 'users':users})


# def index(request):
#     return render(request, "blogs/signup.html")
    
