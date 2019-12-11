
import numpy as np
import numpy.random as npr

from src.svm.full import classify


def test_classify():

    n = 100

    class1 = npr.rand(n // 2, 2)
    class2 = npr.rand(n // 2, 2) + np.array([1, 0])

    theta = np.pi / 8.0
    r = np.cos(theta)
    s = np.sin(theta)
    rotation = np.array([[r, s], [s, -r]])

    samples = np.dot(np.vstack([class1, class2]), rotation)

    labels = np.zeros(n)

    half = n // 2

    labels[:half] = -1
    labels[half:] = 1

    p, q, g, h, x = classify(samples, labels)

    assert type(x).__name__ == 'matrix'

