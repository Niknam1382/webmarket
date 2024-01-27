from django.contrib import admin
from website.models import *
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('first_name', 'last_name', 'email', 'subject', 'created_date')
    empty_value_display = "-empty-"
    list_filter = ('email',)
    search_fields = ('name','message')
    
admin.site.register(ContactForm,ContactAdmin)
admin.site.register(Newsletters)