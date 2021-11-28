from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.db import models
from django.forms import forms
from my_app.models import NavbarModel
from django.shortcuts import redirect, render

from my_app.backends import UserModel
from .models import AboutModel, ContactModel, Footer, NavbarModel, PostImageModel, PostModel, Settings
from .forms import ContactForm, PostCreateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

@login_required(login_url='login_page')

def base_view(request):
    context = {}
    
    navbar_queryset = NavbarModel.objects.all()
    settings_queryset = Settings.objects.all().first
    footer_queryset = Footer.objects.all()

    context['navbar_queryset'] = navbar_queryset
    context['settings_queryset'] = settings_queryset
    context['footer_queryset'] = footer_queryset

    return render(request, 'base.html', context)
    


def home_view(request):
    context = {}
    
    post_queryset = PostModel.objects.filter(is_active=True)
    navbar_queryset = NavbarModel.objects.all()
    settings_queryset = Settings.objects.all().first
    footer_queryset = Footer.objects.all()

    context['post_queryset'] = post_queryset
    context['navbar_queryset'] = navbar_queryset
    context['settings_queryset'] = settings_queryset
    context['footer_queryset'] = footer_queryset
    
    return render(request, 'index.html', context)

def about_view(request):
    context = {}

    about_queryset = AboutModel.objects.all().first()

    context['about_queryset'] = about_queryset

    return render(request,'about.html', context)

def contact_view(request):
    context = {}

    contact_queryset = ContactModel.objects.all().first()
    form = ContactForm()

    context['contact_queryset'] = contact_queryset
    context['form'] = form
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home_page')
        
        else:
            context['form'] = form
            messages.error(request, form.errors)
            return render(request, 'contact.html', context)
    
    return render(request, 'contact.html', context)

def post_create_view(request):
    context = {}
    form = PostCreateForm()
    settings_queryset = Settings.objects.all().first
    context['settings_queryset'] = settings_queryset

    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            form = form.save(commit = False)
            form.user_id = request.user
            form.save()
            return redirect('home_page')
        
        else:
            messages.error(request, form.errors)
            context['form'] = form
            return render(request, 'post_create.html', context)

    context['form'] = form
    return render(request, 'post_create.html', context)

def post_view(request, post_id):
    context = {}

    post_detail_queryset = PostModel.objects.filter(id=post_id).first()
    post_detail_images = PostImageModel.objects.filter(post_id=post_id)

    context['post_detail_queryset'] = post_detail_queryset
    context['post_detail_images'] = post_detail_images

    return render(request, 'post.html', context)


def logout_view(request):
    auth.logout(request)
    return redirect('login_page')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login_page')
    if UserModel.is_active == False :
        pass
        


# def register_view(request):
#     context = {}
#     form = UserCreationForm()
#     settings_queryset = Settings.objects.all().first
#     context['settings_queryset'] = settings_queryset

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             return redirect('login_page')

#         else:
#             context['form'] = form
#             messages.error(request, form.errors)
#             return render(request, 'register.html', context)

#     else:
#         context['form'] = form
#         form = UserCreationForm()
    
#     return render(request, 'register.html', context)

# def login_view(request):
#     context = {}
#     settings_queryset = Settings.objects.all().first
#     context['settings_queryset'] = settings_queryset
    
#     username = request.POST.get("username")
#     raw_password = request.POST.get("password")
#     user = authenticate(username=username, password=raw_password)
    
#     if user:
#         login(request, user)
#         return redirect('home_page')

#     else:
#         context['error_message'] = 'error!'
#         return render(request, 'login.html', context)