from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # image
    # category
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    published_date = models.DateTimeField(null=True)
    views = models.BigIntegerField(default=0)
    # tag
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']
        # verbose_name = 'پست'
        # verbose_name_plural = 'پست ها'

    def __str__(self):
        return f"{self.title} - {self.id}"
    
  