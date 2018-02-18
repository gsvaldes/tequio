import json as jsonlib

import bleach

from django.utils.html import mark_safe
from django.template import Library

register = Library()


@register.filter
def json(value):
    """
    safe jsonify filter, bleaches the json string using
    the bleach html tag remover
    """
    uncleaned = jsonlib.dumps(value)
    clean = bleach.clean(uncleaned)
    return mark_safe(clean)
