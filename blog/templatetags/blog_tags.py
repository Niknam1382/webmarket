from django import template
from blog.models import Post, category

register = template.Library()

@register.inclusion_tag('archive.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    category = category.objects.all()
    cat_dict = {}
    for name in category:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}