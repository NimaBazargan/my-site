from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # image
    # category
    # author
    published_date = models.DateTimeField(null=True)
    views = models.BigIntegerField(default=0)
    # tag
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)