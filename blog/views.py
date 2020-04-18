from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
from .forms import EditPost, CreateUserForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as dj_login, logout, authenticate
from django.contrib.auth.admin import User
from django.contrib import messages


# Create your views here.

def Home_blog(request):
    posts = Post.objects.all().order_by('-pub_date')
    post1 = Post.objects.all()[0]

    context = {"posts": posts, 'post1': post1}
    return render(request, 'blog/index.html', context)



def category(request):
    context = {}
    return render(request, 'blog/category.html', context)



def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    contact = 'contact'
    dic = {'contact': contact}
    return render(request, 'blog/contact.html', dic)

def particular_blog(request, pk):
    blog = get_object_or_404(Post, pk=pk)
    context = {'blog': blog}
    return render(request, 'blog/single-standard.html', context)


@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = EditPost(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('draft')
    else:
        form = EditPost()
        context = {'form': form}
    return render(request, 'blog/edit_post.html', context)


@login_required(login_url='login')
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(request.__dict__)
    if request.method == 'POST':
        form = EditPost(request.POST, request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.last_edited = timezone.now()
            post.save()
            return redirect('blog', pk=post.pk)
    else:
        form = EditPost(instance=post)
        context = {'form': form}
    return render(request, 'blog/edit_post.html', context)


@login_required(login_url='login')
def draft_post(request):
    posts = Post.objects.filter(pub_date__isnull=True).order_by('-pub_date')
    context = {'posts': posts}
    return render(request, 'blog/draft.html', context)


@login_required(login_url='login')
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('/', pk=post.pk)


@login_required(login_url='login')
def post_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog', pk=pk)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.author = request.user
                user.save()
                user_name = form.cleaned_data.get('username')
                messages.success(request, f'successfully created user {user_name}')
                return redirect('login')

        dic = {'form': form}
        return render(request, 'blog/register.html', dic)


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                dj_login(request, user)
                return redirect('home')
            else:
                messages.warning(request, ' invalid username or password')

        return render(request, 'blog/login.html')


def logoutpage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def comment_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.created_date = timezone.now()
            comment.save()
            return redirect('blog', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comments.html', {'form': form})


@login_required(login_url='login')
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog', pk=comment.post.pk)


