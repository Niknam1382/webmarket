from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('folder/archive.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    category = Category.objects.all()
    cat_dict = {}
    for name in category:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}