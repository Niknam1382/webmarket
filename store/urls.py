from django.urls import path
from store.views import *
app_name = 'store'

urlpatterns = [
    path('', store_views, name='home'),
]