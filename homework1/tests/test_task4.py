from task4 import calculate_discount

# A test for ensuring the func works with 2 floats
def test_task4_test_both_float():
    assert calculate_discount(99.99, 45.5) == 54.49455

# A test for ensuring the func works with a float as price int as discount
def test_task4_test_price_float():
    assert calculate_discount(99.99, 5) == 94.9905

# A test for ensuring the func works with a float as discount int as price
def test_task4_test_dicount_float():
    assert calculate_discount(100, 45.5) == 54.5

# A test for ensuring the func works with 2 ints
def test_task4_test_both_int():
    assert calculate_discount(100, 5) == 95.0