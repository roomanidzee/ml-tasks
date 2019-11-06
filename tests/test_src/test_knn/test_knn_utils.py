import numpy as np

from src.knn.utils import convert_df_to_np


def test_convert_df_to_np(test_df):

    np_arr, labels = convert_df_to_np(test_df)

    assert isinstance(np_arr, np.ndarray)
    assert isinstance(labels, list)
    assert isinstance(labels[0], str)
