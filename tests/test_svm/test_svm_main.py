
import random

import numpy as np

from src.svm.main import (
    gram_matrix,
)


def test_predict(predictor_fixture):
    result = predictor_fixture.predict(
        np.array(
            [
                random.choice(list(range(10)))
                for _ in range(10)
            ]
        )
    )

    assert isinstance(result, float)


def test_gram_matrix(test_numpy_arrays):

    result = gram_matrix(test_numpy_arrays[0])
    assert isinstance(result, np.ndarray)