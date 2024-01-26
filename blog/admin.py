from django.contrib import admin
from blog.models import Post, Category
# Register your models here.
'''
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = ('created_at')
    empty_value_display = ('-empty-')
    list_display = ['title','author','created_at','published_at','status']
    list_filter = ['status']
    search_fields = ['title','content','author']
    summernote_fields = ('content',)
'''
admin.site.register(Post)
admin.site.register(Category)