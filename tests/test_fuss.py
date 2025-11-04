from src.fuss import fuss
import pytest


@pytest.mark.parametrize("a,b,expected",[(5,2,1),(6,4,2),(17,3,2)])

def test_fusses(a,b,expected):
    assert fuss(a,b) >= 1

