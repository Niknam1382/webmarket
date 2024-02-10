from django import template

register = template.Library()

@register.filter
def times(number):
    return range(number)

@register.filter
def times_n(number):
    return range(5-number)