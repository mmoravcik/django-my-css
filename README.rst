=============
Django-my-CSS
=============

Simple django app that allows end-users to change CSS. At the moment only
through admin interface.


Instalation
-----------
1. `pip install -e git+git://github.com/mmoravcik/django-my-css.git#egg=django-my-css`
2. add `django-my-css` to `INSTALLED_APPS`

USAGE
-----
In template, use template tag `{% load my_css %}`

and then
`<link href="{% mycss 0 %}" rel="stylesheet" type="text/css" />`

Where the optional parameter is:
0 - css file will be suffixed with random string to avoid caching
1 - cache friendly version (default)

Settings
--------

**MY_CSS_FILENAME**
Filename of generated CSS file. Default is 'mycss.css'

**MY_CSS_URL**
URL where the filename will be accessed from. Default is settings.MEDIA_URL + '/css/'

**MY_CSS_ROOT**
PATH where the file is stored. Default is settings.MEDIA_ROOT + '/css/'

**MY_CSS_ARCHIVE_LIFE**
Life of the archived CSS in days, 0 = no archive, default 200


TODO
----
* Web interface, only django-admin one ATM

