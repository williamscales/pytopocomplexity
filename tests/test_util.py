#!/usr/bin/env python3
# coding=utf-8

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import (ascii, bytes, chr, dict, filter, hex, input, int,
                             map, next, oct, open, pow, range, round, str,
                             super, zip)

import numpy as np
from numpy.linalg import norm
from numpy.random import random_sample

from pytopocomplexity.util import normalize


def test_normalize_zero_vector():
    """Test that passing the zero vector to `normalize` returns the zero
    vector.

    """
    x = np.zeros(3)
    assert (normalize(x) == x).all()


def test_normalize_unit_vector():
    """Test that passing the unit vector to `normalize` returns the unit vector.

    """
    x = np.ones(3)
    assert norm(normalize(x)) == 1


def test_normalize():
    """Test that normalize correctly normalizes a non-unit vector."""
    x = random_sample((3,))
    assert norm(normalize(x)) == 1
