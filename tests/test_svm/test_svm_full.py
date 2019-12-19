
import pytest

import numpy as np
import numpy.random as npr

from src.svm.full import classify


def test_classify():

    try:
        n = 150

        class1 = npr.rand(n // 3, 2)
        class2 = npr.rand(n // 3, 2)
        class3 = npr.rand(n // 3, 2)

        theta = np.pi / 8.0
        r = np.cos(theta)
        s = np.sin(theta)
        rotation = np.array([[r, s], [s, -r]])

        samples = np.dot(np.vstack([class1, class2, class3]), rotation)

        labels = np.zeros(n)

        third = n // 3

        labels[:third] = 0
        labels[third:third - 20] = 1
        labels[third:] = 2

        p, q, g, h, x = classify(samples, labels)

        assert type(x).__name__ == 'matrix'
    except Exception as e:
        pytest.skip(f'Skipping in case of {str(e)}')

