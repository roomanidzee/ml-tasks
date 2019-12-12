import numpy as np
import cvxopt

from src.svm.utils import calculate_util

MULTIPLIER = 1e-5
COEF = 0.1


class Predictor:

    def __init__(self, bazis, weights, vectors, labels):
        self.bazis = bazis
        self.weights = weights
        self.vectors = vectors
        self.labels = labels

    def predict(self, x):

        result = self.bazis

        for z, x_temp, y in zip(self.weights, self.vectors, self.labels):
            result += z * y * calculate_util(x_temp, x)

        return np.sign(result).item()


def gram_matrix(x):
    n_samples, n_features = x.shape
    K = np.zeros((n_samples, n_samples))
    for i, x_i in enumerate(x):
        for j, x_j in enumerate(x):
            K[i, j] = calculate_util(x_i, x_j)
    return K


def lagrange_magic(X, y):
    n_samples, n_features = X.shape

    K = gram_matrix(X)

    P = cvxopt.matrix(np.outer(y, y) * K)
    q = cvxopt.matrix(-1 * np.ones(n_samples))

    G_std = cvxopt.matrix(np.diag(np.ones(n_samples) * -1))
    h_std = cvxopt.matrix(np.zeros(n_samples))

    G_slack = cvxopt.matrix(np.diag(np.ones(n_samples)))
    h_slack = cvxopt.matrix(np.ones(n_samples) * COEF)

    G = cvxopt.matrix(np.vstack((G_std, G_slack)))
    h = cvxopt.matrix(np.vstack((h_std, h_slack)))

    A = cvxopt.matrix(y, (1, n_samples))
    b = cvxopt.matrix(0.0)

    solution = cvxopt.solvers.qp(P, q, G, h, A, b)

    return np.ravel(solution['x'])


def prepare_predictor(X, y, lagrange):
    indices = lagrange > MULTIPLIER

    multipliers = lagrange[indices]
    vectors = X[indices]
    labels = y[indices]

    predictor = Predictor(
        bazis=0.0,
        weights=multipliers,
        vectors=vectors,
        labels=labels
    )

    bazis = np.mean(
        [
            y_k - predictor.predict(x_k)
            for(y_k, x_k) in zip(labels, vectors)
        ]
    )

    return Predictor(
        bazis,
        multipliers,
        vectors,
        labels
    )


def train(X, y):
    lagrange = lagrange_magic(X, y)
    return prepare_predictor(X, y, lagrange)
