import pytest
from test_calcul2 import addition
@pytest.mark.parametrize("a,b,resultat", [
    (1,2,3),
    (10,20,30),
    (5,5,10),
    (15,5,20)
])