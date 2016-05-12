

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    """
    Notes
    =====
    * rel_tol is a relative tolerance, it is multiplied by the greater
    of the magnitudes of the two arguments; as the values get larger,
    so does the allowed difference between them while still considering them equal.
    * abs_tol is an absolute tolerance that is applied as-is in all cases.
    If the difference is less than either of those tolerances,
    the values are considered equal. 
    """
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
