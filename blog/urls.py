from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed

app_name = 'blog'

urlpatterns = [
    path('',index_view,name='index'),
    path('post/<int:pid>/',single_view,name='single'),
    path('category/<str:cat_name>/',index_view,name='category'),
    path('author/<str:author_username>/',index_view,name='author'),
    path('search/',index_view,name='search'),
    path('tag/<str:tag_name>/',index_view,name='tag'),
    path("rss/feed/", LatestEntriesFeed()),
]