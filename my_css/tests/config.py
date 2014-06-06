from django.conf import settings


def configure():
    if not settings.configured:
        test_settings = {
            'DATABASES': {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                },
            },
            'INSTALLED_APPS': [
                'django.contrib.auth',
                'django.contrib.admin',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.sites',
                'django.contrib.flatpages',
                'django.contrib.staticfiles',

                'my_css',
                ],
            'PASSWORD_HASHERS': ['django.contrib.auth.hashers.MD5PasswordHasher'],

        }

        settings.configure(**test_settings)
