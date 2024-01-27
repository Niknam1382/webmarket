from django.shortcuts import render
from website.forms import *
# Create your views here.
def index(request) :
    if request.method == 'POST' :
        form = NewsletterForm(request.POST)
        if form.is_valid() :
            form.save()
    form = NewsletterForm()
    return render(request, 'index.html', {'form': form})

def contact(request) :
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid() :
            form.save()
    form = ContactForm()
    return render(request, 'contact.html')