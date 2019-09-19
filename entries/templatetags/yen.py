from django import template

register = template.Library()

@register.filter(name='yen')
def yen(value):
    length = len(str(value))
    if length == 6:
        return '{:,}'.format(value)