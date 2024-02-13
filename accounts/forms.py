from django import forms
from accounts.models import UserForm

class UserForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = '__all__'