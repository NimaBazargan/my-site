from django import template
from blog.models import Post
from django.shortcuts import get_object_or_404
from django.utils import timezone

register = template.Library()

@register.simple_tag(name='counted_views')
def function(pid):
    posts = Post.objects.filter(status = 1, published_date__lte=timezone.now())
    post = get_object_or_404(posts,id=pid)
    post.views += 1
    post.save()
    return post.views

@register.inclusion_tag('prev-next.html')
def show_prev_next(pid):
    posts = Post.objects.filter(status = 1, published_date__lte=timezone.now())
    post = get_object_or_404(posts,id=pid)
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
    return context



