from src.add_a_b_c import add


def test_add():
    assert add(1,0,1)==2

def test_add02():
    assert add(5,3,1)==9

def test_add03():
    assert add(7,2,-1)==8
