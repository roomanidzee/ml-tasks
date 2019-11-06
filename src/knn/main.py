from typing import List

from src.commons.types import Float, Integer
import numpy as np

import operator


def classify(
        input_data: List[Float],
        arr_data: np.ndarray,
        labels: List[str],
        k: Integer
) -> str:

    input_size = arr_data.shape[0]
    matrix_diff = np.tile(input_data, (input_size, 1)) - arr_data

    diff_square = matrix_diff ** 2
    dist_square = diff_square.sum(axis=1)
    final_dist = dist_square ** 0.5
    sorted_dist = final_dist.argsort()

    label_count = {}

    for i in range(k):

        temp = labels[sorted_dist[i]]
        label_count[temp] = label_count.get(temp, 0) + 1

    sorted_labels = sorted(
        label_count.items(),
        key=operator.itemgetter(1),
        reverse=True
    )

    return sorted_labels[0][0]
