from django.shortcuts import render
from website.forms import NewsletterForm
# Create your views here.
def index(request) :
    if request.method == 'POST' :
        form = NewsletterForm(request.POST)
        print(form)
        if form.is_valid() :
            form.save()
    form = NewsletterForm()
    return render(request, 'index.html', {'form': form})