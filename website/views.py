from django.shortcuts import render, HttpResponseRedirect
from website.forms import *
from django.contrib import messages
from website.models import News

from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request) :
    if request.method == 'POST' :
        form = NewsletterForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.add_message(request, messages.SUCCESS, "ایمیل شما با موفقیت برای عضویت در خبرنامه ثبت شد")
        else:
            messages.add_message(request, messages.ERROR, "درخواست شما با خطا مواجه شد")
    form = NewsletterForm()
    return render(request, 'index.html', {'form': form})

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
