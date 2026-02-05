from task4 import calculate_discount

def test_task4_test_both_float():
    assert calculate_discount(99.99, 45.5) == 54.49455

def test_task4_test_price_float():
    assert calculate_discount(99.99, 5) == 94.9905

def test_task4_test_dicount_float():
    assert calculate_discount(100, 45.5) == 54.5

def test_task4_test_both_int():
    assert calculate_discount(100, 5) == 95.0