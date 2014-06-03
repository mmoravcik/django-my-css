import uuid

from my_css import settings
from django import template

register = template.Library()


@register.simple_tag()
def my_css(cache=1):
    css_file = settings.MY_CSS_URL + settings.MY_CSS_FILENAME
    if not cache:
        css = "%s?u=%s" % (css_file, str(uuid.uuid4())[:8])
    return css