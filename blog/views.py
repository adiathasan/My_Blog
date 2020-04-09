from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
from .forms import EditPost
# Create your views here.

def Home_blog(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    post1 = Post.objects.all()[0]
    context = {"posts": posts, 'post1': post1}
    return render(request, 'blog/index.html', context)

def category(request):
    context = {}
    return render(request, 'blog/category.html', context)

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def perticular_blog(request, pk):
    blog = get_object_or_404(Post, pk=pk)
    context = {'blog': blog}
    return render(request, 'blog/single-standard.html', context)

def edit_post(request):
    if request.method == 'POST':
        form = EditPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog', pk=post.pk)
    else:
        form = EditPost()
        context = {'form': form}
    return render(request, 'blog/edit_post.html', context)
