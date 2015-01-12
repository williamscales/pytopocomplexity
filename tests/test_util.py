#!/usr/bin/env python3
# coding=utf-8
"""Tests for `pytopocomplexity.util`"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import (ascii, bytes, chr, dict, filter, hex, input, int,
                             map, next, oct, open, pow, range, round, str,
                             super, zip)

import numpy as np
from numpy.linalg import norm
from numpy.random import random_integers, random_sample

from pytopocomplexity.util import normalize, sample_box


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
    """Test that normalize correctly normalizes a random non-unit vector."""
    x = random_sample((3,))
    assert np.isclose([norm(normalize(x))], [1]).all()


def test_sample_box():
    """Test that `sample_box` generates the proper number of samples within the
    correct bounds.

    """
    # Generate some random bounds
    bounds = []
    bounds_count = 0
    num_dimensions = random_integers(2, 10)
    while bounds_count < num_dimensions:
        candidate_bound = random_sample(2)
        low, high = candidate_bound
        if low > high:
            candidate_bound = [high, low]
        bounds.append(candidate_bound)
        bounds_count += 1

    num_samples = random_integers(100)
    points = sample_box(bounds, num_samples)

    assert len(points) == num_samples

    results = np.empty([num_samples, num_dimensions])
    for counter, point in enumerate(points):
        for axis, value in enumerate(point):
            low = bounds[axis][0]
            high = bounds[axis][1]
            results[counter, axis] = (low <= value <= high)
    assert results.all()
