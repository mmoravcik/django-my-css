#!/usr/bin/env python
"""
Installation script:
"""

from setuptools import setup, find_packages


setup(
    name='django-my-css',
    version='0.0.1',
    url='https://github.com/mmoravcik/django-my-css',
    author="Matus Moravcik",
    author_email="matus.moravcik@gmail.com",
    description="Simple app that allows user to change "
                "CSS of Django app in admin",
    long_description=open('README.rst').read(),
    keywords="css",
    license='BSD',
    platforms=['linux'],
    packages=find_packages(exclude=["sandbox*", "tests*"]),
    include_package_data=True,
    install_requires=[
        'django=>1.2',
    ],
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: Unix',
                 'Programming Language :: Python']
    )
