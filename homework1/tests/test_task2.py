import task2

def test_int_type():
    assert isinstance(task2.x, int)
    assert task2.x == 12

def test_float_type():
    assert isinstance(task2.y, float)
    assert task2.y == 5.99

def test_str_type():
    assert isinstance(task2.sent, str)
    assert task2.sent == "Cheeseburger"

def test_bool_type():
    assert isinstance(task2.bo, bool)
    assert task2.bo == True