from django.shortcuts import render, get_object_or_404, redirect
from store.models import *
from accounts.models import *
from django.utils import timezone
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from django.contrib import messages

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


# @login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST["product_id"]
        cart_item = Cart.objects.get(user=request.user, product=product_id)
        # print(cart_item)
        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
            # messages.success(request, "Item added to your cart.")
            messages.add_message(request, messages.SUCCESS,"محصول مورد نظر به سبد خرید شما اضافه شد")
        else:
            Cart.objects.create(user=request.user, product=product_id)
            messages.add_message(request, messages.SUCCESS,"محصول مورد نظر به سبد خرید شما اضافه شد")

    return redirect('/store')

# @login_required
'''
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")

    return redirect("cart:cart_detail")
'''
# @login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    # item_quantity = Cart.objects.filter(user=request.user).quantity
    # total_price = sum(item.quantity * item.product.price for item in cart_items)
    c = 1
    for i in cart_items:
        i = str(i)
        t = i.split(' ')[2]
    print(t)
    context = {
        # 'item_quantity':item_quantity,
        "cart_items": cart_items,
        # "total_price": total_price,
    }

    return render(request, "checkout-step-1.html", context)


'''
def add_to_cart(request):
    product_ids = request.session.get('product_ids', {})  # Retrieve product_ids from session
    print(product_ids)
    if request.method == 'GET':
        pid = request.GET.get("pid")
        prod = get_object_or_404(product, status=True, pk=pid)
        if str(prod.id) not in product_ids:
            product_ids[str(prod.id)] = 1
        else:
            product_ids[str(prod.id)] += 1
        print(product_ids)
        

        request.session['prods'] = product_ids
        # if 'cart' not in request.session:
        #     request.session['cart'] = {}
        # request.session['cart'].extend(product_ids)
    return redirect('/store')

def view_cart(request):
    my_data = request.session.get('prods', {})
    cart_products = dict()
    for i in my_data.keys():
        cart_products[get_object_or_404(product, status=True, pk=i)] = my_data[i]
    # cart_products = product.objects.filter(id__in=my_data)
    # cart_product_ids = request.session.get('cart', [])
    # cart_products = product.objects.filter(id__in=cart_product_ids)
    return render(request, 'checkout-step-1.html', {'cart_products': cart_products})

def remove_from_cart(request, product_id):
    product = get_object_or_404(product, pk=product_id)
    if 'cart' in request.session:
        request.session['cart'].remove(product.id)
    return redirect('/store')
'''