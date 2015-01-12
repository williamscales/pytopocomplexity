#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utility functions used by other modules"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import (ascii, bytes, chr, dict, filter, hex, input, int,
                             map, next, oct, open, pow, range, round, str,
                             super, zip)

from numpy import asarray
from numpy.linalg import norm
from numpy.random import random_sample


def normalize(x):
    """Given a vector, return the normalized vector

    Parameters
    ----------
    x : array-like
        Vector to be normalized

    Returns
    -------
    x_normed : array-like
        Normalized version of `x` (i.e. ``np.abs(x_normed) == 1``)

    """
    x = asarray(x)
    x_norm = norm(x)
    if x_norm == 0:
        return x
    return x/x_norm


def sample_box(bounds, num_samples):
    """Uniformly randomly sample an n-dimensional box.

    Parameters
    ----------
    bounds : list
        A list of n 2-tuples corresponding to the lower and upper bounds of each
        of the n coordinate axes.
    num_samples : int
        The number of random points to generate

    Returns
    -------
    points : array-like
        An array of shape (num_points, n), where n is the number of dimensions.

    """
    num_dimensions = len(bounds)

    # Find out by how much we must scale the random numbers
    lowest = None
    highest = None
    for (low, high) in bounds:
        if (((lowest is not None) and (low < lowest)) or
            (lowest is None)):
            lowest = low
        if (((highest is not None) and (high > highest)) or
            (highest is None)):
            highest = high

    # Generate samples uniformly and throw away the ones that are outside
    # the bounds
    points = []
    sample_counter = 0
    while sample_counter < num_samples:
        point = (highest - lowest)*random_sample(num_dimensions) + lowest
        reject = False
        for axis, value in enumerate(point):
            low = bounds[axis][0]
            high = bounds[axis][1]
            if not low <= value <= high:
                reject = True
        if not reject:
            points.append(point)
            sample_counter += 1

    return points
