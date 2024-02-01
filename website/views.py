from django.shortcuts import render, HttpResponseRedirect
from website.forms import *
from django.contrib import messages

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