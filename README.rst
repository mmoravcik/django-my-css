=============
Django-my-CSS
=============

Simple django app that allows end-users to change CSS. At the moment only
through the admin interface.

.. image:: https://api.travis-ci.org/mmoravcik/django-my-css.svg?branch=master
    :target: https://travis-ci.org/mmoravcik/django-my-css

.. image:: https://coveralls.io/repos/mmoravcik/django-my-css/badge.png?branch=master
    :target: https://coveralls.io/r/mmoravcik/django-my-css?branch=master

How to Use
==========

Get the code
------------

Not in pip yet::

   $ pip install -e git+git://github.com/mmoravcik/django-my-css.git#egg=django-my-css

Install in your project
-----------------------

Register 'my_css' in the 'INSTALLED_APPS' section of
your project's settings. ::

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.admin',
        'django.contrib.sites',
        'django.contrib.comments',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.contenttypes',

        'my_css',
    )


Templates Usage
----------------

All of the examples assume that you first load the my_css template tag in
your template.::

    {% load my_css_tags %}


Add this to your HEAD section of the template. ::

    <link href="{% my_css 0 %}" rel="stylesheet" type="text/css" />


Where the optional parameter is:
0 - css file will be suffixed with random string to avoid caching
1 - cache friendly version (default)

Configuration
-------------

Optional configuration settings, which you can set in your Django settings file

* ``MY_CSS_FILENAME``
Filename of generated CSS file. Default is ``mycss.css``

* ``MY_CSS_URL``
URL where the filename will be accessed from. Default is ``settings.MEDIA_URL + '/css/'``

* ``MY_CSS_ROOT``
PATH where the file is stored. Default is ``settings.MEDIA_ROOT + '/css/'``

* ``MY_CSS_ARCHIVE_LIFE``
Life of the archived CSS in days, 0 = no archiving, default is 200


TODO
----
* web interface, only django-admin one ATM
* include in pip
* migrations

