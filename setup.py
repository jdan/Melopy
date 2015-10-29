#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

config = {
    'name': 'Melopy',
    'author': 'Jordan Scales',
    'author_email': 'scalesjordan@gmail.com',
    'description': 'Python music library',
    'long_description': open('README.txt').read(),
    'packages': ['melopy'],
    'version': '0.1.1',
    'url': 'https://github.com/jdan/Melopy',
    'license': 'LICENSE.txt',
    'classifiers': []
}

setup(**config)

# Licensed under The MIT License (MIT)
# See LICENSE file for more
