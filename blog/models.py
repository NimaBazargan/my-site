from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', default= 'blog/default.jpg')
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    published_date = models.DateTimeField(null=True)
    views = models.BigIntegerField(default=0)
    tag = models.ManyToManyField(Tag)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']
        # verbose_name = 'پست'
        # verbose_name_plural = 'پست ها'

    def __str__(self):
        return f"{self.title} - {self.id}"
    
    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})
    
  