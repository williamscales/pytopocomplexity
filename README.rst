pytopocomplexity
================
.. image:: https://travis-ci.org/williamscales/pytopocomplexity.svg?branch=master
   :alt: Travis CI build status
   :target: https://travis-ci.org/williamscales/pytopocomplexity

Overview
--------
pytopocomplexity is an object-oriented Python library which provides generic
algorithms for estimating the topographic complexity of higher dimensional
energy landscapes. Additionally, some examples are included.

Requirements
------------
pytopocomplexity requires the following:
* future
* numpy
* scipy

Additionally, if you want to build the documentation and run the tests you need:
* sphinx
* pytest

You can get a complete development environment by installing and setting up
virtualenv and virtualenvwrapper following this guide_ and then running the
following::

$ mkvirtualenv pytopocomplexity --python=$(which python3.4)
$ workon pytopocomplexity
$ pip install -r /path/to/pytopocomplexity/requirements.txt

If you want Python 2.6, 2.7, or 3.4 instead (these are the supported versions),
just replace the python3.4 in the example above with python2.6, python2.7, or
python3.3.

.. _guide: http://docs.python-guide.org/en/latest/dev/virtualenvs/

License
-------
Copyright 2014 William Scales

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License.  You may obtain a copy of the
License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied.  See the License for the
specific language governing permissions and limitations under the License.
