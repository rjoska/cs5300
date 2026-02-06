import numpy as np
import task7

def test_task7_types():
    assert isinstance(task7.A_matrix, np.ndarray)
    assert isinstance(task7.b_vector, np.ndarray)

def test_task7_some_linalg_ret1():
    ret1, doNotUse = task7.do_some_linalg()
    expected = np.array([1.0, 12.0])
    assert np.allclose(ret1, expected)

def test_task7_some_linalg_ret2():
    doNotUse, ret2 = task7.do_some_linalg()
    inverse = np.array([
        [0.5, 0.0],
        [0.0, 4.0]
    ])
    assert np.allclose(ret2, inverse)