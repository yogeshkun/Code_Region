from django import template

register = template.Library()
@register.simple_tag
def update_variable(bolle= None):
    print(bolle)
    """Allows to update existing variable in template"""
    return bolle

register.filter('update_variable', update_variable)

