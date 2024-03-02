from django import template
from accounts.models import Cart
from django.contrib.auth.decorators import login_required

register = template.Library()

@register.inclusion_tag('folder/cart.html')
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = 0
    total_product = 0
    for i in cart_items:
        total_price += (i.product.price * i.quantity)
        total_product += i.quantity
    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "total_product":total_product
    }
    return context