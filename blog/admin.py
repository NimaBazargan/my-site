from django.contrib import admin
from blog.models import Post

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title',)
    # exclude = ('title',)
    list_display = ('title' ,'views','status','published_date','created_date')
    list_filter = ('status',)
    ordering = ['created_date']
    search_fields = ['title','content']

admin.site.register(Post,PostAdmin)
