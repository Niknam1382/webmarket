from django.shortcuts import render, HttpResponseRedirect
from website.forms import *
from django.contrib import messages
from website.models import News
from store.models import product
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request) :
    now = timezone.now()
    news = News.objects.all().order_by('-date')[:5]
    if len(news) > 0 :
        newsd = 1
    else:
        newsd = 0
    products = product.objects.filter(status=True).exclude(published_at__gt=now).order_by('-published_at')[:6]
    products_off = product.objects.filter(status=True, price_off__isnull=False).exclude(published_at__gt=now).order_by('-published_at')
    try:
        products_star = product.objects.filter(status=True, star=5).exclude(published_at__gt=now).order_by('-published_at')
        if len(products_star) < 4:
            try:
                products_star = product.objects.filter(status=True, star__in=[5,4]).exclude(published_at__gt=now).order_by('-published_at')
            except:
                pass
            if len(products_star) < 4:
                try:
                    products_star = product.objects.filter(status=True, star__in=[5,4,3]).exclude(published_at__gt=now).order_by('-published_at')
                except:
                    pass
                if len(products_star) < 4:
                    try:
                        products_star = product.objects.filter(status=True, star__in=[5,4,3,2]).exclude(published_at__gt=now).order_by('-published_at')
                    except:
                        pass
                    if len(products_star) < 4:
                        try:
                            products_star = product.objects.filter(status=True, star__in=[5,4,3,2,1]).exclude(published_at__gt=now).order_by('-published_at')
                        except:
                            pass
    except:
        pass
    if request.method == 'POST' :
        form = NewsletterForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.add_message(request, messages.SUCCESS, "ایمیل شما با موفقیت برای عضویت در خبرنامه ثبت شد")
        else:
            messages.add_message(request, messages.ERROR, "درخواست شما با خطا مواجه شد")
    form = NewsletterForm()
    return render(request, 'index.html', {'form': form, 'products': products, 'products_off':products_off, 'products_star':products_star, 'news':news, 'newsd':newsd})

def contact(request) :
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid() :
            form.save()
    form = ContactForm()
    return render(request, 'contact.html')

def SendEmail(request):
    if request.method == 'POST' :
        subject = request.POST['subject']
        content = request.POST['content']
        x = News.objects.create(send=True)
        x.subject = subject
        x.content = content
        x.save()
        message = content
        email_from = settings.EMAIL_HOST_USER
        n = Newsletters.objects.all()
        recipient_list = ['nik.webmarket@gmail.com', ]
        for i in n :
            i = str(i)
            i = i.split(' - ')[0]
            recipient_list.append(i)
        send_mail( subject, message, email_from, recipient_list )
    return render(request, 'news.html')

def website_search(request):
    now = timezone.now()
    prod = product.objects.filter(status=1).exclude(published_at__gt=now)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            products = prod.filter(description__contains=s).order_by('-published_at')
    context = {'products': products}
    return render(request,'shop.html', context)

def about_us(request):
    return render(request, 'about-us.html')