from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('website/website-latest.html')
def latest_post(arg=6):
    posts = Post.objects.filter(status = 1, published_date__lte=timezone.now()).order_by("-published_date")
    posts = posts[:arg]
    context = {
        'posts' : posts
    }
    return context
    