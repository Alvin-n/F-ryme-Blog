from django import forms
from django.forms import fields
from my_app.models import ContactModel, PostModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['name', 'subtitle', 'text', 'head_image', 'tags']

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')

# class PostForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorUploadingWidget())