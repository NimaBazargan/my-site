from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from taggit.models import Tag
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import CommentForm
from django.contrib import messages

def index_view(request,**kwargs):
    posts = Post.objects.filter(status = 1, published_date__lte=timezone.now())
    tags = Tag.objects.all()
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tag__name__in = [kwargs['tag_name']])
    if request.method == 'GET':
        if q := request.GET.get('q'):
            posts = posts.filter(content__contains = q)
    posts = Paginator(posts,2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.page(posts.num_pages)
    context = {
        'posts': posts,
        'tags': tags,
    }
    return render(request,'blog/blog-home.html',context)

def single_view(request,**kwargs):
    posts = Post.objects.filter(status = 1, published_date__lte=timezone.now())
    post = get_object_or_404(posts,id=kwargs['pid'])
    tags = Tag.objects.all()
    comments = Comment.objects.filter(post=kwargs['pid'], approved=True)
    if kwargs.get('cid'):
        parent = kwargs['cid']
    else: 
        parent = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'success')
        else:
                for errors in form.errors.values():
                    for error in errors:
                        messages.add_message(request,messages.ERROR,f'{error}')
        return redirect('blog:single',pid=post.id)
    else:
        form = CommentForm()
    context = {
        'post' : post,
        'tags': tags,
        'comments': comments,
        'form':form,
        'parent': parent,
    }
    return render(request,'blog/blog-single.html',context)

def category_view(request,name):
    posts = Post.objects.filter(status = 1, published_date__lte=timezone.now())
    posts = posts.filter(category__name= name)
    context = {
        'posts':posts,
    }
    return render(request,'blog/blog-home.html',context)