#!/usr/bin/env python3
# coding=utf-8
"""Tests for `pytopocomplexity.entropy`"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import (ascii, bytes, chr, dict, filter, hex, input, int,
                             map, next, oct, open, pow, range, round, str,
                             super, zip)

import numpy as np
from numpy.random import random_sample

from pytopocomplexity.entropy import estimate_entropy


def test_entropy_is_zero_for_unimodal_function():
    """Test that the entropy of a function with one extremum is zero."""
    def func_one_min(x):
        """Objective function with global minimum at ``x == 0``."""
        return x**2
    #initial_models = 2*random_sample((100,100)) - 1
    initial_models = 2*random_sample(100) - 1
    entropy = estimate_entropy(func_one_min, initial_models, 1e-8, 1e5)
    assert entropy == 0
