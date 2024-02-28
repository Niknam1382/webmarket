from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('signup', signup_view, name='signup'),
    path('reset', reset_view, name='reset'),
    path('change', change_view, name='change'),
    path('profile', profile_view, name='profile'),
    path('change2', change_2, name='change2'),
]