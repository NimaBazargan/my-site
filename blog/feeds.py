from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post
from django.utils import timezone


class LatestEntriesFeed(Feed):
    title = "blog newest post"
    link = "/rss/feed"
    description = "latest post pf blog"

    def items(self):
        return Post.objects.filter(status = 1, published_date__lte=timezone.now()).order_by("-published_date")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content