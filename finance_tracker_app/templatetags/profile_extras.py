import os
from django import template
from django.conf import settings

register = template.Library()

@register.filter
def image_exists(image_field):
    if not image_field:
        return False
    path = os.path.join(settings.MEDIA_ROOT, str(image_field))
    return os.path.isfile(path) 