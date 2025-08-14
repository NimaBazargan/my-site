from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

def index_view(request):
    posts = Post.objects.filter(status = 1, published_date__lte=timezone.now())
    context = {
        'posts': posts,
    }
    return render(request,'blog/blog-home.html',context)

def single_view(request,pid):
    posts = Post.objects.filter(status = 1, published_date__lte=timezone.now())
    post = get_object_or_404(posts,id=pid)
    context = {
        'post' : post,
    }
    return render(request,'blog/blog-single.html',context)

def category_view(request,name):
    posts = Post.objects.filter(status = 1, published_date__lte=timezone.now())
    posts = posts.filter(category__name= name)
    context = {
        'posts':posts,
    }
    return render(request,'blog/blog-home.html',context)

