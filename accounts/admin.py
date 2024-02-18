from django.contrib import admin
from accounts.models import *
# Register your models here.
# class CartAdmin(admin.ModelAdmin):
#     date_hierarchy = ('updated_at')
#     empty_value_display = ('-empty-')
#     list_display = ['user','product','updated_at','is_paid']
#     list_filter = ['user']
    
admin.site.register(Cart)