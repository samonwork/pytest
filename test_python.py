import python

def test_add():
    assert python.add(7, 5) == 12
    assert python.add(7) == 9

def test_product():
    assert python.product(7, 5) == 35
    assert python.product(7) == 14