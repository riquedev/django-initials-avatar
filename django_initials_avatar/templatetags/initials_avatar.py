from django import template
from django.template.defaultfilters import stringfilter
import gettext

register = template.Library()


@register.filter
@stringfilter
def language_code_to_iso2(value: str):
    lang = value.split("-")
    if len(lang) > 1:
        return lang[1]
    else:
        expand = gettext._expand_lang(value)
        if len(expand) > 1:
            return str(expand[1].split("_")[-1]).lower()

    return ""
