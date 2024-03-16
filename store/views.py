from django.shortcuts import render, get_object_or_404, redirect
from store.models import *
from accounts.models import *
from django.utils import timezone
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.forms import CartD2Form
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from store.forms import StoreCommentForm

# Create your views here.
def store_views(request):
    now = timezone.now()
    products = product.objects.filter(status=True).exclude(published_at__gt=now).order_by('-published_at')
    t = product.objects.filter(status=False)
    for i in products:
        for j in t:
            if i.name==j.name:
                if i.price_off == j.price:
                    pass
                else:
                    j.delete()
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

def category_views(request, cat_name):
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
    comments = StoreComment.objects.filter(product=prod.id, approved=True)
    context = {'prod':prod, 'prodc':prodc, 'comments':comments}
    return render(request,'product.html', context)

def product_comment(request):
    if request.method == 'POST':
        form = StoreCommentForm(request.POST)
        prod_id = int(request.POST.get('product'))
        starf = int(request.POST.get('star'))
        P = product.objects.get(id=prod_id)
        P.star_c += 1
        P.star_t += starf
        P.star = P.star_t // P.star_c
        P.save()
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, 'کامنت شما در صف بررسی قرار گرفت')
        else:
            messages.add_message(request,messages.ERROR, 'کامنت شما ثبت نشد')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def add_to_cart(request):
    if request.method == 'GET':
        product_id = int(request.GET.get("product_id"))
        try:
            num = int(request.GET.get("num"))
        except:
            num = None
        if num == None:
            num = 1
        prod = product.objects.get(pk=product_id)
        if prod.price_off is not None:
            new_prod = product.objects.get_or_create(name=prod.name, price=prod.price_off, image=prod.image, inventory=prod.inventory)
            cart_item = None
            try:
                cart_item = Cart.objects.get(user=request.user, product=new_prod[0])
            except:
                pass
            if cart_item:
                cart_item.quantity += num
                cart_item.save()
                messages.add_message(request, messages.SUCCESS,"محصول به سبد شما اضافه شد")
            else:
                cart_item = Cart.objects.create(user=request.user, product=new_prod[0], quantity=num)
        else:
            cart_item = None
            try:
                cart_item = Cart.objects.get(user=request.user, product=prod)
            except:
                pass
            if cart_item:
                cart_item.quantity += num
                cart_item.save()
                messages.add_message(request, messages.SUCCESS,"محصول به سبد شما اضافه شد")
            else:
                cart_item = Cart.objects.create(user=request.user, product=prod, quantity=num)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=int(cart_item_id))
    if cart_item.user == request.user:
        cart_item.delete()
        messages.add_message(request, messages.SUCCESS,"محصول با موفقیت از سبد خرید شما حذف شد")
    return redirect('/store/cart_detail')

@login_required
def remove_from_cart2(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=int(cart_item_id))
    if cart_item.user == request.user:
        cart_item.delete()
        messages.add_message(request, messages.SUCCESS,"محصول با موفقیت از سبد خرید شما حذف شد")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = 0
    for i in cart_items:
        total_price += (i.product.price * i.quantity)
    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }
    return render(request, "checkout-step-1.html", context)

@login_required
def cart_refresh(request):
    if request.method == 'GET':
        cart_items = Cart.objects.filter(user=request.user)
        for i in cart_items:
            p = 'p' + str(i.id)
            prod = request.GET.get(p)
            cart_item = Cart.objects.get(user=request.user, pk=prod)
            x = 'n' + str(i.id)
            n = request.GET.get(x)
            cart_item.quantity = n
            cart_item.save()
        messages.add_message(request, messages.SUCCESS,"تازه سازی سبد خرید شما با موفقیت انجام شد")
    return redirect('/store/cart_detail')

@login_required
def cart_detail2(request):
    if request.method == 'POST':
        form = CartD2Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            first_name = data['first_name']
            last_name = data['last_name']
            phone_number = data['phone_number']
            city = data['city']
            email = data['email']
            address1 = data['address1']
            address2 = data['address2']
            code_posti = data['code_posti']
            request.session['first_name'] = first_name
            request.session['last_name'] = last_name
            request.session['phone_number'] = phone_number
            request.session['city'] = city
            request.session['email'] =email
            request.session['address1'] = address1
            request.session['address2'] = address2
            request.session['code_posti'] = code_posti
            return redirect('/store/cart_detail_3')
        else:
            messages.add_message(request, messages.WARNING,"شما محصولی در سبد خرید خود ندارید")
    form = CartD2Form()
    return render(request,"checkout-step-2.html", {'form': form})

@login_required
def cart_detail3(request):
    if request.method == 'POST':
        options = request.POST['options']
        request.session['options'] = options
        return redirect('/store/cart_detail_4')
    return render(request,"checkout-step-3.html")

@login_required
def cart_detail4(request):
    t = False
    if request.method == 'POST':
        confirm = request.POST['confirm']
        if confirm == 'confirm':
            t = True
    cart_items = Cart.objects.filter(user=request.user)
    total_price = 0
    for i in cart_items:
        total_price += (i.product.price * i.quantity)
    first_name = request.session.get('first_name')
    last_name = request.session.get('last_name') 
    phone_number = request.session.get('phone_number')
    city = request.session.get('city')
    email = request.session.get('email')
    address1 = request.session.get('address1')
    address2 = request.session.get('address2')
    code_posti = request.session.get('code_posti')
    options = request.session.get('options')
    if options == 'offline':
        cart = Cart.objects.filter(user = request.user)
        c = RegisteredCart()
        c.user = request.user
        c.first_name = first_name
        c.last_name = last_name
        c.phone_number = phone_number
        c.city = city
        c.email = email
        c.address1 = address1
        c.address2 = address2
        c.code_posti = code_posti
        x = True
        l = []
        for single_cart in cart:
            c.cart = single_cart
            single_cart.product.inventory -= single_cart.quantity
            if single_cart.product.inventory < 0:
                x = False
            l.append((single_cart.product.name,single_cart.quantity))
        if x is False:
            messages.add_message(request, messages.warning,"برای اطلاع از تعداد موجودی تماس بگیرید")
        else:
            single_cart.product.save()
            c.save()

            subject = 'اطلاعیه سفارش آفلاین'
            txt1 = f'سفارش دهنده : {first_name} {last_name}'
            txt2 = f'نام کاربری : {request.user.username}'
            txt3 = f'{email} \n {city}'
            txt4 = f'{phone_number}'
            txt5 = f'{address1}'
            txt6 = f'{address2}'
            txt7 = f'کد پستی : {code_posti}'
            txt8 = ''
            for i in l:
                txt8 += f'{i[0]} - {i[1]}\n'
                
            txt = f'{txt1}\n{txt2}\n{txt3}\n{txt4}\n{txt5}\n{txt6}\n{txt7}\n{txt8}'
            if t is True:
                message = txt
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['nik.webmarket@gmail.com', ]
                send_mail( subject, message, email_from, recipient_list )
                messages.add_message(request, messages.SUCCESS,"سفارش شما در صف بررسی قرار رفت و نتیجه ی آن به شما ارسال میشود")
                cart.delete()
                return redirect('/')
        
    elif options == 'online':
        if t is True:
            return redirect('http://127.0.0.1:8000/zarinpal/request/')
    else:
        pass
    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }
    return render(request,"checkout-step-4.html", context)