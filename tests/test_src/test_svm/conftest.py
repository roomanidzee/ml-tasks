
import numpy as np

import pytest


@pytest.fixture
def random_arrays():
    return np.random.rand(3,2), np.random.rand(3,2)
