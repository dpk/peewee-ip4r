#!/usr/bin/env python
"""
peewee-ip4r
-----------

Support for the ip4r extensions to PostgreSQL for Peewee.
"""

from distutils.core import setup

setup(
  name = 'peewee-ip4r',
  version = '0.1',
  description = 'Support for the ip4r extensions to PostgreSQL for Peewee',
  author = 'David P. Kendal',
  author_email = 'pypi@dpk.io',
  url = 'https://github.com/dpk/peewee-ip4r',
  py_modules = ['peewee_ip4r'],
  keywords = ['postgresql', 'postgres', 'peewee', 'ip', 'ip4r', 'internet'],
  classifiers = [
    'License :: Public Domain',
    'Topic :: Database :: Front-Ends',
    'Programming Language :: Python :: 3.5'
  ]
)
