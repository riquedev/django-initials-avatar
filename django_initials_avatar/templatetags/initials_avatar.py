from django import template
from django.urls import reverse
from urllib.parse import urlencode

register = template.Library()


@register.simple_tag
def render_initials_avatar(name, **kwargs):
    kwargs['name'] = name
    return f"%s?{urlencode(kwargs)}" % reverse('initials-avatar-svg')
