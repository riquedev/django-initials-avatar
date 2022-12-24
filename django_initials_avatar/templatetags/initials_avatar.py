from django import template
from django.urls import reverse
from urllib.parse import urlencode

register = template.Library()


@register.simple_tag
def render_initials_avatar(name, **kwargs):
    kwargs['name'] = name

    if kwargs.get("old_method"):
        # ( https://github.com/riquedev/django-initials-avatar/issues/1#issuecomment-1352677054 )
        return f"%s?{urlencode(kwargs)}" % reverse('initials-avatar-svg')

    return f"{reverse('initials-avatar-svg')}?{urlencode(kwargs)}"
