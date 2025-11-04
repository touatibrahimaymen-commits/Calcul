from src.add_a_b_c import add
import pytest


@pytest.mark.parametrize("a,b,c,expected_resolt",
                         [(2,3,5,10),(1,2,3,6)] )
def test_add_a_b_c_expected_resolt(a,b,c,expected_resolt):
    assert add(a,b,c) == expected_resolt

