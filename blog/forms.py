from django.forms import ModelForm
from blog.models import Comment

class CommentForm(ModelForm) :
    class Meta:
        model = Comment
        fields = ['post','user','first_name','last_name','message']