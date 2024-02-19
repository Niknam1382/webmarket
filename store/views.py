from django.shortcuts import render, get_object_or_404, redirect
from store.models import *
from accounts.models import *
from django.utils import timezone
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    '''
    request.session['product_ids'] = {}
    '''
    context = {'prod':prod, 'prodc':prodc}
    return render(request,'product.html', context)


@login_required
def add_to_cart(request):
    if request.method == 'GET':
        product_id = int(request.GET.get("product_id"))
        prod = product.objects.get(pk=product_id)
        cart_item = None
        try:
            cart_item = Cart.objects.get(user=request.user, product=prod)
        except:
            pass
        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item = Cart.objects.create(user=request.user, product=prod)
    return redirect('/store')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)
    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")

    return redirect("cart:cart_detail")

@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    # item_quantity = Cart.objects.filter(user=request.user).quantity
    total_price = 0
    for i in cart_items:
        total_price += (i.product.price * i.quantity)
    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(request, "checkout-step-1.html", context)