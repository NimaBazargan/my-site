from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

# @admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title',)
    # exclude = ('title',)
    list_display = ['title' ,'author','views','status','published_date','created_date',]
    list_filter = ['status','author',]
    # ordering = ['created_date']
    search_fields = ['title','content',]
    summernote_fields = ['content',]

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['post','name','approved','created_date',]
    list_filter = ['post','approved',]
    search_fields = ['name','post',]

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
# admin.site.register(Tag)
