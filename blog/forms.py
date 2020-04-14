from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User


class EditPost(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'text', 'category', 'image', ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['comment', ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2', ]
