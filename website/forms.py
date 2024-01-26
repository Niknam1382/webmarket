from django import forms
from website.models import Newsletters

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletters
        fields = '__all__'