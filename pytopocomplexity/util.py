#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utility functions used by other modules"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import (ascii, bytes, chr, dict, filter, hex, input, int,
                             map, next, oct, open, pow, range, round, str,
                             super, zip)

from numpy.linalg import norm


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
    x_norm = norm(x)
    if x_norm == 0:
        return x
    return x/x_norm
