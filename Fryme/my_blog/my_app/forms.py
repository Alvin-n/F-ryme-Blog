from django import forms
from django.forms import fields
from .models import ContactModel, PostModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['name', 'subtitle', 'text', 'head_image', 'tags']