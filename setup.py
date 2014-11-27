#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import (ascii, bytes, chr, dict, filter, hex, input, int,
                             map, next, oct, open, pow, range, round, str,
                             super, zip)

from os import path
import sys

from setuptools import setup, find_packages


def read(file):
    """ Reads and returns as a string the contents of a file.

    Parameters
    ----------
    file : str
        Path to the file to be read, relative to the directory where setup.py is
        located

    Returns
    -----
    output : str
        The contents of `file`.

    """
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, file), encoding='utf-8') as f:
        output = f.read()
    return output


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    package_name = 'pytopocomplexity'
    package_version = '0.1'
    homepage_url = 'https://github.com/williamscales/pytopocomplexity'
    package_author = 'William Scales'
    package_author_email = 'william@wscales.com'
    license = 'Apache Software License'
    short_description = 'Algorithms using entropy to estimate complexity of'
                        ' high dimensional functions'
    long_description = read('README.rst')
    required = [
        'future',
        'numpy',
        'scipy',
    ]
    extras = {
        'develop': [
            'sphinx',
            'pytest',
        ]
    }
    classifiers = [
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    keywords = 'complexity, optimization'

    setup(
        name=package_name,
        version=package_version,
        description=short_description,
        long_description=long_description,
        url=homepage_url,
        author=package_author,
        author_email=package_author_email,
        license=license,
        platforms='OS Independent',
        classifiers=classifiers,
        keywords=keywords,
        packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
        install_requires=required,
        extras_require=extras,
    )

if __name__ == '__main__':
    sys.exit(main())
