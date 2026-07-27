from django import template
from django.conf import settings
from pathlib import Path

register = template.Library()

@register.filter
def split(value, delimiter):
    if value:
        return value.split(delimiter)
    return []

@register.filter
def strip(value):
    if value:
        return value.strip()
    return value

@register.filter
def media_fallback(file_field, fallback_static_path):
    if not file_field:
        return fallback_static_path
    try:
        file_path = Path(settings.MEDIA_ROOT) / file_field.name
        if file_path.exists():
            return file_field.url
    except Exception:
        pass
    return fallback_static_path
