import calculator

def test_add():
    assert calculator.add(3, 4) == 7

def test_sub():
    assert calculator.sub(10, 3) == 7

def test_mul():
    assert calculator.mul(3, 5) == 15

def test_div():
    assert calculator.div(10, 2) == 5
