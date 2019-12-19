
from typing import Tuple

import numpy as np

from src.log_reg.utils import calculate_sigmoid, calculate_gradient


def train(
  data: np.ndarray,
  input_labels: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray]:

    m, n = data.shape
    labels = np.zeros(input_labels.shape)

    label_names = np.unique(input_labels)
    label_numbers = range(len(label_names))

    for elem in zip(label_names, label_numbers):
        old_name = elem[0]
        new_name = elem[1]
        labels[np.where(input_labels == old_name)] = new_name

    labels = labels.reshape((len(labels), 1))
    theta_init = np.zeros((n, 1))

    return calculate_gradient(data, labels, theta_init)


def classify(
  data: np.ndarray,
  thetas: np.ndarray,
) -> np.ndarray:

    return np.round(
        calculate_sigmoid(
            np.dot(data, thetas)
        ),
    )
