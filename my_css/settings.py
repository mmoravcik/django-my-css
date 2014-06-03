from django.conf import settings


MY_CSS_FILENAME = getattr(settings, 'MY_CSS_FILENAME', 'mycss.css')
MY_CSS_URL  = getattr(settings, 'MY_CSS_URL', settings.MEDIA_URL + '/css/')
MY_CSS_ROOT = getattr(settings, 'MY_CSS_ROOT', settings.MEDIA_ROOT + '/css/')
# Life of the archived CSS in days, 0 = no archive
MY_CSS_ARCHIVE_LIFE = getattr(settings, 'MY_CSS_ARCHIVE_LIFE', 200)