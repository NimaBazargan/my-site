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
    post.views += 1
    post.save()
    index = list(posts).index(post)
    prev_post = list(posts)[index-1]
    len_list = len(list(posts))-1
    if index != len_list:
        next_post = list(posts)[index+1]
    else:
        next_post = list(posts)[0]
    context = {
        'post' : post,
        'posts' : posts,
        'index': index,
        'len_list': len_list,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    return render(request,'blog/blog-single.html',context)


