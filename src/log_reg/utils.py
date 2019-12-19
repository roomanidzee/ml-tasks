
from typing import Tuple

import numpy as np

ALPHA = 2.0
NUM_ITER = 100
LAMBDA_VAL = 0


def calculate_sigmoid(
        data: np.ndarray,
) -> np.ndarray:

    data = np.array(data, dtype=np.longdouble)

    return 1 / (1 + np.exp(-data))


def theta_cost_compute(
        data: np.ndarray,
        labels: np.ndarray,
        init_theta: np.ndarray,
) -> np.ndarray:

    m, n = data.shape

    theta_range = range(1, init_theta.shape[0])
    theta_value = init_theta[theta_range, :]

    reg_parameter = np.dot(
        LAMBDA_VAL / (2 * m),
        np.sum(theta_value ** 2)
    )

    logar_data = np.log(
        calculate_sigmoid(np.dot(data, init_theta))
    )

    constant = -1.0

    j = (constant / m) * np.sum(
        logar_data * labels + np.log(1 - logar_data) * (1 - labels)
    )

    return j + reg_parameter


def calculate_gradient(
        data: np.ndarray,
        labels: np.ndarray,
        init_theta: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray]:

    m, n = data.shape

    cost = theta_cost_compute(data, labels, init_theta)

    for elem in range(NUM_ITER):
        cost = theta_cost_compute(data, labels, init_theta)

        B = calculate_sigmoid(np.dot(data, init_theta) - labels)
        A = np.array((1 / m) * np.transpose(data))
        gradient = np.dot(A, B)

        for i in range(1, len(gradient)):
            A = list(np.array(calculate_sigmoid(np.dot(data, init_theta)) - labels))
            B = list(np.array((data[:, i].reshape((data[:, i].shape[0], 1)))))

            result = []

            for elem1, elem2 in zip(A, B):
                result.append(elem1[0] + elem2[0])

            gradient[i] = np.array(sum(result))

        init_theta = init_theta - (
            np.dot(
                (ALPHA / m),
                gradient
            )
        )

    return init_theta, cost
