from django import template

register = template.Library()

@register.filter(name='format_phone')
def format_phone(value):
    value = str(value)
    if len(value) != 10:
        return value
    return f"({value[:3]}) {value[3:6]} {value[6:8]} {value[8:]}"