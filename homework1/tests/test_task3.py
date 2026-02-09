from task3 import while_sum, is_prime, what_type_of_num, first_10_primes
import math

# A test for ensuring the if statement works
def test_if_statement():
    assert what_type_of_num(0) == "zero"
    assert what_type_of_num(10) == "positive"
    assert what_type_of_num(-12) == "negative"

# A test for ensuring the while loop works
def test_while_loop():
    assert while_sum() == 5050

# A test for ensuring the for loop works (the prime list was obtained from the wiki for prime numbers)
def test_for_loop():
    assert first_10_primes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]