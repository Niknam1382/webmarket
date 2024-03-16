from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('niknews',SendEmail, name='niknews'),
    path('search', website_search, name='search'),
    path('about_us',about_us, name='about_us'),
]