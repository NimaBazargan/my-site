from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

def index_view(request,**kwargs):
    posts = Post.objects.filter(status = 1, published_date__lte=timezone.now())
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username = kwargs['author_username'])
    if request.method == 'GET':
        if q := request.GET.get('q'):
            posts = posts.filter(content__contains = q)
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