from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index_view(request):
    posts = Post.objects.filter(status = 1)
    context = {
        'posts': posts,
    }
    return render(request,'blog/blog-home.html',context)

def single_view(request):
    return render(request,'blog/blog-single.html')

def test_view(request,id):
    posts = get_object_or_404(Post,id=id)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/test.html',context)
