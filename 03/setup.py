#!/usr/bin/env python3

from setuptools import setup

def requires(filename='requirements.txt'):
    """Yields a list of all pip requirements

    :param filename: the pip requirement filename
            (usually 'requirements.txt')
    :yield: name of a library
    """
    with open(filename, 'r+t') as pipreq:
        for line in pipreq:
            line = line.strip()
            if not line or \
                line.startswith('#') or \
                line.startswith('-r'):
                    continue
            yield line


setup(
    # -- Project information
    name='tuxfish',
    version='0.1.0',
    author='Tux Penguin',
    author_email='tux (AT) example.org',
    url='https://github.com/tomschr/python-project',
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

    # Requirements:
    install_requires=list(requires()),

    # -- Script(s):
    scripts=['bin/tuxfish.py'],
    )
