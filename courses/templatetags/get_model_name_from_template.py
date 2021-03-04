from django import template

register = template.Library()

@register.filter()
def get_model_name(val):
    return val.__class__.__name__
