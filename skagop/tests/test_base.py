#############################################################################
# A few test classes

import numpy as np
from ..base import AggregationOperator

class MeanAggregation(AggregationOperator):
    def fuse(self, a):
        return np.sum(a)
    def arity(self):
        return float(inf)

#############################################################################
# The tests

import random


def test_minimal_conditions(operator=MeanAggregation()):
    check_scalar(operator)
    check_boundary(operator)
    check_nondecreasing(operator)

def check_scalar(operator):
    """Tests the "identity when unary" condition."""
    if operator.arity == 1:
        a = random.random()
        assert(operator.fuse(a)==a)

def check_boundary(operator):
    """Tests the boundary conditions."""

    pass

def check_nondecreasing(operator):
    """Tests the 'non-decreasing' condition"""
    pass
