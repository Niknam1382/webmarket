from django.shortcuts import render

# Create your views here.
def store_views(request):
    return render(request,'shop.html')