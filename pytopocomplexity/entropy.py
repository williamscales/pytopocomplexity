#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Estimate the entropy of a given objective function."""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import (ascii, bytes, chr, dict, filter, hex, input, int,
                             map, next, oct, open, pow, range, round, str,
                             super, zip)

import numpy as np

from pytopocomplexity.search import random_hill_climbing
from pytopocomplexity.util import normalize


def estimate_entropy(objective_function, initial_models, tolerance,
                     max_iterations):
    """Estimate entropy of an objective function.

    Parameters
    ----------
    objective_function : function
        Objective function whose entropy will be estimated
    initial_models : array-like
        Array containing initial models. These should be chosen uniformly at
        random from the model space
    tolerance : float
        Tolerance corresponding to the stopping criteron for RHC
    max_iterations: int
        Maximum number of iterations for RHC search

    Returns
    -------
    entropy : float
        A statistical estimate of the topological entropy of the objective
        function

    """
    converged_models, frequencies = random_hill_climbing(objective_function,
                                                         initial_models,
                                                         tolerance,
                                                         max_iterations)
    num_minima = len(converged_models)

    function_values = np.array([objective_function(m) for m in
                                converged_models])

    min_function_values = np.full([num_minima], function_values.min())
    normed_function_values = np.abs(function_values - min_function_values)
    sigma = 1/num_minima*np.sum(normed_function_values)

    if sigma == 0:
        v = np.zeros([num_minima])
    else:
        v = np.exp(-np.abs(function_values - min_function_values)/sigma)

    x = frequencies/len(initial_models)

    q_unnormed = x*v
    q_normed = normalize(q_unnormed)

    entropy = -np.sum(q_normed*np.log(q_normed))

    return entropy
