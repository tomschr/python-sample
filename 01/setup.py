#!/usr/bin/env python3

from setuptools import setup

setup(
    # -- Project information
    name='tuxfish',
    version='0.1.0',
    url='https://github.com/tomschr/python-project',
    author='Tux Penguin',
    author_email='tux (AT) example.org',
    license='GPL-3.0',
    keywords='example, Tux, fish',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
      'Development Status :: 5 - Production/Stable'
      #
      'Intended Audience :: Developers',
      # The license:
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      # Supported Python versions:
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
    ],

    # -- Description:
    description='Makes a lot of fish',
    long_description='...',

    # -- Script(s):
    scripts=['bin/tuxfish.py'],
    )
