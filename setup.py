#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from builtins import *

from codecs import open
from os import path
import sys

from setuptools import setup, find_packages


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    here = path.abspath(path.dirname(__file__))

    # Get the long description from the relevant file
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

    setup(
        name='pytopocomplexity',
        version='0.1',
        description='Algorithms using entropy to estimate complexity of high'
                    'dimensional functions',
        long_description=long_description,
        url='https://github.com/williamscales/pytopocomplexity',
        author='William Scales',
        author_email='william@wscales.com',
        license='MIT',
        platforms='OS Independent',
        classifiers=[
            'Development Status :: 1 - Planning',
            'Environment :: Console',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
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
            'Topic :: Scientific/Engineering :: Physics'
        ],
        keywords='complexity, optimization',
        packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
        install_requires=[
            'future',
            'numpy',
        ],
    )

if __name__ == '__main__':
    sys.exit(main())
