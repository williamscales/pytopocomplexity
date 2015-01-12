#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Search algorithms"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import (ascii, bytes, chr, dict, filter, hex, input, int,
                             map, next, oct, open, pow, range, round, str,
                             super, zip)

from numpy import isclose
from scipy.optimize import fmin_cg


def random_hill_climbing(func, initial_models, tolerance=None,
                         max_iterations=None):
    """Minimize a given function using a random hill climbing strategy

    Parameters
    ----------
    func: function
        Objective function for which we will find minima.
    initial_models : array-like
        Array containing initial models. These should be chosen uniformly at
        random from the model space.
    tolerance : float
        Gradients must be reduced below this tolerance for the search to stop.
    max_iterations: int
        Maximum number of iterations for the search.

    Returns
    -------
    minima : array-like
        The local minima found after optimizing the function.
    frequencies : array-like
        The number of times the search converged to a given model.

    """
    minima = []
    frequencies = []
    for initial_model in initial_models:
        minimum = fmin_cg(func, initial_model, gtol=1e-6)
        if len(minima) > 0:
            for index, m in enumerate(minima):
                if isclose([minimum], [m]).all():
                    frequencies[index] += 1
                    break
                minima.append(minimum)
                frequencies.append(1)
        else:
            minima = [minimum]
            frequencies = [1]

    return (minima, frequencies)
