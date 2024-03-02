from django.urls import path
from store.views import *

app_name = 'store'

urlpatterns = [
    path('', store_views, name='home'),
    path('category/<str:cat_name>',category_views, name='category'),
    path('<int:pid>',product_views, name='product'),
    path('add_to_cart',add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<str:cart_item_id>',remove_from_cart, name='remove_from_cart'),
    path('remove_from_cart2/<str:cart_item_id>',remove_from_cart2, name='remove_from_cart2'),
    path('cart_detail',cart_detail, name='cart_detail'),
    path('cart_refresh',cart_refresh, name='cart_refresh'),
    path('cart_detail_2',cart_detail2, name='cart_detail2'),
    path('cart_detail_3',cart_detail3, name='cart_detail3'),
    path('cart_detail_4',cart_detail4, name='cart_detail4'),
]