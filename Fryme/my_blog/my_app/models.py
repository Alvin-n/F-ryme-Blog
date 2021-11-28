from os import memfd_create, urandom
from  django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.contrib import admin
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
#from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(default=False)
    

class NavbarModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

class Settings(models.Model):
    background_image = models.ImageField(upload_to ='blog_images', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to ='blog_images', null=True, blank=True)

class Footer(models.Model):
    logo_image = models.ImageField(upload_to ='blog_images', null=True, blank=True)
    logo_url = models.URLField(null=True, blank=True)

class PostModel(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField(auto_now=True)
    text = RichTextField(null=True, blank=True) #models.TextField(null=True, blank=True)
    head_image = models.ImageField(upload_to ='blog_images')
    tags = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)

class AboutModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    background_image = models.ImageField(upload_to ='blog_images', null=True, blank=True)

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=140)
    text = models.TextField(max_length=150, null=True, blank=True)

class PostImageModel(models.Model):
    post_id = models.ForeignKey('PostModel', on_delete=CASCADE)
    images = models.ImageField(upload_to = 'blog_images', null=True, blank=True)



'''
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, help_text="Slug will be generated automatically from the title of the post")    
    content = RichTextUploadingField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
'''