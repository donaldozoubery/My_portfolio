from django import template

register = template.Library()

@register.filter
def split(value, delimiter):
    """
    Split a string by delimiter and return a list
    Usage: {{ "tag1,tag2,tag3"|split:"," }}
    """
    if value:
        return value.split(delimiter)
    return []

@register.filter
def strip(value):
    """
    Strip whitespace from string
    Usage: {{ "  text  "|strip }}
    """
    if value:
        return value.strip()
    return value
