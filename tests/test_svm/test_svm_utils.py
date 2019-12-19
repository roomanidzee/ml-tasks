import numpy as np
from src.svm.utils import calculate_util


def test_calculate_util(test_numpy_arrays):

    first = test_numpy_arrays[0]
    second = test_numpy_arrays[1]

    assert isinstance(calculate_util(first, second), np.ndarray)
