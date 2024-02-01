from django.contrib import admin
from blog.models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = ('created_at')
    empty_value_display = ('-empty-')
    list_display = ['title','author','created_at','published_at','status']
    list_filter = ['status']
    search_fields = ['title','content','author']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = ('created_at')
    empty_value_display = ('-empty-')
    list_filter = ['post', 'approved']
    search_fields = ['name', 'post', 'subject', 'message']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)