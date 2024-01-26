from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_home, name='blog'),
    path('<int:pid>', blog_single, name = 'single'),
    path('category/<str:cat_name>', blog_category, name = 'category'),
    path('author/<str:author_username>', blog_home, name='author'),
    path('search/', blog_search, name='search'),
]