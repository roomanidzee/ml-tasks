
from cvxopt import solvers, matrix

import logging

logger = logging.getLogger(__name__)

c = 1.0


def classify(samples, labels):
    n = len(samples[0])

    p = matrix(0.0, (n + 1, n + 1))
    for i in range(n):
        p[i, i] = 1.0

    q = matrix(0.0, (n + 1, 1))
    q[-1] = 1.0

    m = len(samples)
    h = matrix(-1.0, (m, 1))

    g = matrix(0.0, (m, n + 1))
    for i in range(m):
        g[i, :n] = -labels[i] * samples[i]
        g[i, n] = -labels[i]

    x = solvers.qp(p, q, g, h)['x']

    return p, q, h, g, x
