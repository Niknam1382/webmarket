from django import forms
from website.models import *

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletters
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = '__all__'