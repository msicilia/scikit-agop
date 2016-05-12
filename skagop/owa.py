import numpy as np
from base import AggregationOperator

class OWA(AggregationOperator):

    def __init__(self, weights):
        self._weights = weights


    def fuse(self, a):
        """Aggregates the array into a single value.
        It takes a list, tuple of NumPy array as input.
        """
        # Convert in the cases of type other than ndarray
        if type(a) is list or type(a) is tuple:
            a = np.array(a)
        if type(a) is float or type(a) is int:
            a = np.array([a])

        perm = np.sort(a)
        return sum(self._weights*perm)

    def arity(self):
        return self._weights.size 
