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
from pytopocomplexity.util import normalize, sample_box


def compute_entropy(objective_function, bounds):
    """Exactly compute the entropy of an objective function (Definition 1 in the
    paper).

    We will do this using a Monte Carlo method. First we uniformly sample the
    model space. Then we run the models downhill and determine in which basin of
    attraction each one lies. This lets us compute the volume of the basin of
    attraction. Then we can directly compute the entropy.

    Parameters
    ----------
    objective_function : function
        Objective function whose entropy will be computed
    bounds : list
        A list of n 2-tuples corresponding to the lower and upper bounds of each
        of the n coordinate axes.

    Returns
    -------
    entropy : float
        The computed topographical entropy of the objective function.
    """
    num_samples = 100
    points = sample_box(bounds, num_samples)
    minima, frequencies = random_hill_climbing(objective_function, points)
    global_minimum = min(minima)
    num_minima = len(minima)

    # The probability of converging to a given basin of attraction
    probabilities = [f/num_samples for f in frequencies]
    probabilities = normalize(probabilities)
    function_values = [objective_function(m) for m in minima]
    normed_function_values = np.array([np.abs(y - global_minimum) for y in
                                       function_values])
    sigma = 1/num_minima*np.sum(normed_function_values)
    if not np.isclose([sigma], [0]).all():
        probabilities = probabilities*np.exp(-np.abs(function_values -
                                                     global_minimum)/sigma)
        probabilities = normalize(probabilities)

    print(np.sum(probabilities))
    entropy = -np.sum(probabilities*np.log(probabilities))
    return entropy


def estimate_entropy(objective_function, initial_models, tolerance=None,
                     max_iterations=None):
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

    if np.isclose([sigma], [0]).all():
        v = np.ones([num_minima])
    else:
        v = np.exp(-np.abs(function_values - min_function_values)/sigma)

    x = frequencies/len(initial_models)

    q_unnormed = x*v
    q_normed = q_unnormed/np.sum(q_unnormed)

    entropy = -np.sum(q_normed*np.log(q_normed))

    return entropy


if __name__ == '__main__':
    def f(x):
        return np.sin(x)
    bounds = [(0, np.pi)]
    entropy = compute_entropy(f, bounds)
    print(entropy)
