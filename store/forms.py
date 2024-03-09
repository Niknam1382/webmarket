from django.forms import ModelForm
from store.models import Cart_Detail2, StoreComment

class CartD2Form(ModelForm):
     class Meta:
         model = Cart_Detail2
         fields = "__all__"

class StoreCommentForm(ModelForm) :
    class Meta:
        model = StoreComment
        fields = ['product','user','first_name','last_name','message', 'star']