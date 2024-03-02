from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('niknews',SendEmail, name='niknews'),

]