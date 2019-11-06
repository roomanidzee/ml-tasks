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
