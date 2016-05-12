"""Base classes for all operators."""

import numpy as np
from abc import abstractmethod, abstractproperty, ABCMeta

class AggregationOperator(object):
    """Base class for all aggregation operators in scikit-agop
    Notes
    -----
    All operators should specify all the parameters that can be set
    at the class level in their ``__init__`` as explicit keyword
    arguments (no ``*args`` or ``**kwargs``).
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def fuse(self, a):
        """Aggregates an array of values.
        Notes
        -----
        It assumes the array is of numerical values in [0,1],
        and the result is also in [0,1].
        This may entail scaling. You can use sklearn.preprocessing.scale.
        """
        pass

    @abstractproperty
    def arity(self):
        """Returns the arity (number of inputs) of the operator
        Notes
        -----
        For aggregation operators with infinite arity, return float(inf).
        """
        pass
