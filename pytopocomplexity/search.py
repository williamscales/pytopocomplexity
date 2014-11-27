#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Search algorithms"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import (ascii, bytes, chr, dict, filter, hex, input, int,
                             map, next, oct, open, pow, range, round, str,
                             super, zip)

from collections import Counter

import numpy as np
from scipy.optimize import fmin_cg


def random_hill_climbing(func, initial_models, tolerance, max_iterations):
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
    frequencies = Counter()
    for initial_model in initial_models:
        minimum = fmin_cg(func, initial_model, maxiter=max_iterations,
                          gtol=tolerance)
        if frequencies[minimum[0]] == 0:
            minima.append(minimum)
        frequencies[minimum[0]] += 1
    frequencies_list = np.array([frequencies[m[0]] for m in minima])
    return (minima, frequencies_list)
