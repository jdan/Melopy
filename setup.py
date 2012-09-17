#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'name': u'Melopy',
        'author': u'Jordan Scales',
        'author_email': u'none',
        'description': u'Python music library',
        'long_description': open(u'README.txt').read(),
        'packages': ['melopy'],
        'install_requires': [],
        'tests_require': ['nose'],
        'test_suite': u'nose.collector',
        'version': u'0.1.0',
        'url': u'https://github.com/prezjordan/Melopy',
        'license': 'LICENSE.txt',
        'classifiers': [],
}

setup(**config)

# Licensed under The MIT License (MIT)
# See LICENSE file for more

