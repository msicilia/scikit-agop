
from ..owa import OWA
from test_base import test_minimal_conditions

#--------------------------
# Minimal common conditions
#--------------------------

def test_owa():
    test_minimal_conditions(OWA([1.0]))
    test_minimal_conditions(OWA([0.4, 0.3, 0.3]))
