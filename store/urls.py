from django.urls import path
from store.views import *
app_name = 'store'

urlpatterns = [
    path('', store_views, name='home'),
    path('category/<str:cat_name>',category_views, name='category'),
    path('<int:pid>',product_views, name='product')
]