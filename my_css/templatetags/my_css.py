import uuid

from django.conf import settings
from django import template

register = template.Library()


@register.simple_tag()
def my_css(cache=1):
    css = settings.MY_CSS_URL + settings.MY_CSS_FILENAME
    if not cache:
        css = "%s?u=%s" % (css, str(uuid.uuid4()))
    return css