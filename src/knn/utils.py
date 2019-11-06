from typing import List, Tuple

import pandas as pd
import numpy as np


def convert_df_to_np(
        input_df: pd.DataFrame
) -> Tuple[np.ndarray, List[str]]:

    x_column = input_df['x'].tolist()
    y_column = input_df['y'].tolist()
    labels = input_df['label'].tolist()

    data = [
        [elem1, elem2]
        for elem1, elem2 in zip(x_column, y_column)
    ]

    return np.array(data), labels


def normalize_data(
        input_data: np.ndarray
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """For case, if you need to normalize data"""

    min_values = input_data.min(0)
    max_values = input_data.max(0)

    ranges = max_values - min_values
    first_value = input_data.shape[0]

    normalized_data = (input_data - np.tile(min_values, (first_value, 1))) / np.tile(ranges, (first_value, 1))

    return normalized_data, ranges, min_values
