from django.shortcuts import render, get_object_or_404
from store.models import product, Category, brand, size, color
from django.utils import timezone
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)

# Create your views here.
def store_views(request, **kwargs):
    now = timezone.now()
    products = product.objects.filter(status=True).exclude(published_at__gt=now).order_by('-published_at')
    categories = Category.objects.all()
    brands = brand.objects.all()
    sizes = size.objects.all()
    colors = color.objects.all()

    products = Paginator(products, 12)
    try :
        page_number = request.GET.get('page')
        products = products.get_page(page_number)
    except PageNotAnInteger :
        products = products.get_page(1)
    except EmptyPage:
        products = products.get_page(1)
    
    context = {'products': products, 'categories': categories, 'brands': brands, 'sizes': sizes, 'colors':colors}
    return render(request,'shop.html', context)

def category_views(request, cat_name, **kwargs):
    now = timezone.now()
    products = product.objects.filter(status=True, category__name=cat_name).exclude(published_at__gt=now).order_by('-published_at')
    categories = Category.objects.all()
    brands = brand.objects.all()
    sizes = size.objects.all()
    colors = color.objects.all()
    products = Paginator(products, 12)
    try :
        page_number = request.GET.get('page')
        products = products.get_page(page_number)
    except PageNotAnInteger :
        products = products.get_page(1)
    except EmptyPage:
        products = products.get_page(1)
    context = {'products': products, 'categories': categories, 'brands': brands, 'sizes': sizes, 'colors':colors}
    return render(request,'shop.html', context)

def product_views(request, pid):
    prod = get_object_or_404(product, status=True, pk=pid)
    cat = prod.category.get()
    cat = cat.name
    prodc = product.objects.filter(category__name=cat)
    prod.counted_views += 1
    prod.save()
    context = {'prod':prod, 'prodc':prodc}
    return render(request,'product.html', context)