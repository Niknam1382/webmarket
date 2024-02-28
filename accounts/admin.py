from django.contrib import admin
from accounts.models import *

class RegisteredCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'last_name', 'phone_number', 'email']
    list_filter = ['user']

admin.site.register(profile)
admin.site.register(RegisteredCart, RegisteredCartAdmin)
