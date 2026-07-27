from django import template
from django.conf import settings
from pathlib import Path
from django.templatetags.static import static

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
        fallback = fallback_static_path
        if fallback.startswith('static/'):
            return static(fallback[len('static/'):])
        if fallback.startswith('/static/'):
            return static(fallback[len('/static/'):])
        return fallback
    try:
        file_path = Path(settings.MEDIA_ROOT) / file_field.name
        if file_path.exists():
            return file_field.url
    except Exception:
        pass
    fallback = fallback_static_path
    if fallback.startswith('static/'):
        return static(fallback[len('static/'):])
    if fallback.startswith('/static/'):
        return static(fallback[len('/static/'):])
    return fallback
