#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions to compute the entropic complexity of a given objective
function.

"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from future.builtins import (ascii, bytes, chr, dict, filter, hex, input, int,
                             map, next, oct, open, pow, range, round, str,
                             super, zip)

import numpy as np

from pytopocomplexity.search import random_hill_climbing


def compute_entropy(objective_function, local_minima):
    """Exactly compute the entropy of an objective function (Definition 1 in the
    paper).

    We will do this using Monte Carlo methods.

    Parameters
    ----------
    objective_function : function
        Objective function whose entropy will be computed
    local_minima : list
        A list of the distinct, isolated local minima of the objective function.

    Returns
    -------
    entropy : float
        The computed topographical entropy of the objective function.
    """
    pass

def estimate_entropy(objective_function, initial_models, tolerance,
                     max_iterations):
    """Estimate the entropy of an objective function (Definition 2 in the
    paper).

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

    # np.isclose() checks whether floats are epsilon close
    if np.isclose([sigma], [0]).all():
        v = np.ones([num_minima])
    else:
        v = np.exp(-np.abs(function_values - min_function_values)/sigma)

    x = frequencies/len(initial_models)

    q_unnormed = x*v
    q_normed = q_unnormed/np.sum(q_unnormed)

    entropy = -np.sum(q_normed*np.log(q_normed))

    return entropy
