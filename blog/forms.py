from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User


class EditPost(forms.ModelForm):
    class Meta:
        model = Post

<<<<<<< HEAD
        fields = ['title', 'text', 'category', 'image', ]
=======
        fields = ['title', 'text', 'category']
>>>>>>> 949189bd0530dc0648a564d6ca4994ba2bbe18ec


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['comment', ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User

<<<<<<< HEAD
        fields = ['username', 'email', 'password1', 'password2', ]
=======
        fields = ['username', 'email', 'password1', 'password2']
>>>>>>> 949189bd0530dc0648a564d6ca4994ba2bbe18ec
