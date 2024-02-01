from django.contrib import admin
from store.models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class productAdmin(SummernoteModelAdmin):
    date_hierarchy = ('created_at')
    empty_value_display = ('-empty-')
    list_display = ['name','price','updated_at']
    list_filter = ['available']
    search_fields = ['name','description']
    summernote_fields = ('description',)

admin.site.register(product, productAdmin)
admin.site.register(Category)
admin.site.register(color)
admin.site.register(size)