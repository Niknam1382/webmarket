from django.contrib import admin
from accounts.models import *
from django.contrib.auth.models import User

class CartAdmin(admin.ModelAdmin):
    date_hierarchy = ('updated_at')
    empty_value_display = ('-empty-')
    list_display = ['user', 'get_user_first_name', 'get_user_last_name', 'product', 'quantity', 'updated_at', 'is_paid']
    list_filter = ['user']

    def get_user_first_name(self, obj):
        user = User.objects.filter(username=obj.user)
        print(user)
    get_user_first_name.short_description = 'First Name'

    def get_user_last_name(self, obj):
        return obj.user.last_name
    get_user_last_name.short_description = 'Last Name'

admin.site.register(Cart, CartAdmin)