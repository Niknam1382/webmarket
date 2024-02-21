from django.forms import ModelForm
from store.models import Cart_Detail2

class CartD2Form(ModelForm):
     class Meta:
         model = Cart_Detail2
         fields = "__all__"