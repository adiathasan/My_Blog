from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
class EditPost(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'text', ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2']

