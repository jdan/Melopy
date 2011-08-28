#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

config = {
        'name': u'Melopy',
        'author': u'Jordan Scales',
        'author_email': u'',
        'description': u'Python music library',
        'long_description': open(u'README.markdown').read(),
        'packages': find_packages(),
        'install_requires': [],
        'tests_require': ['nose'],
        'test_suite': u'nose.collector',
        'version': u'',
        'url': u'https://github.com/prezjordan/Melopy',
        'classifiers': [],
}

setup(**config)

# Licensed under The MIT License (MIT)
# See LICENSE file for more

