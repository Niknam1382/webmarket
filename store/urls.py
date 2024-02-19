from django.urls import path
from store.views import *
app_name = 'store'

urlpatterns = [
    path('', store_views, name='home'),
    path('category/<str:cat_name>',category_views, name='category'),
    path('<int:pid>',product_views, name='product'),
    path('add_to_cart',add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>',remove_from_cart, name='remove_from_cart'),
    path('cart_detail',cart_detail, name='cart_detail'),
]