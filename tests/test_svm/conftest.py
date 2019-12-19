
import random

import pytest
import numpy as np

from src.svm.main import Predictor


@pytest.fixture
def predictor_fixture(test_numpy_arrays):
    return Predictor(
        bazis=0.6,
        weights=np.array(
            [
                random.choice(list(range(10)))
                for _ in range(10)
            ]
        ),
        vectors=np.array(
            [
                random.choice(list(range(10)))
                for _ in range(10)
            ]
        ),
        labels=np.array(
            [
                random.choice(list(range(10)))
                for _ in range(10)
            ]
        )
    )
