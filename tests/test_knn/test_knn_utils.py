import numpy as np

from src.knn.utils import convert_df_to_np, normalize_data


def test_convert_df_to_np(test_df):

    np_arr, labels = convert_df_to_np(test_df)

    assert isinstance(np_arr, np.ndarray)
    assert isinstance(labels, list)
    assert isinstance(labels[0], str)


def test_normalize_data(test_df):
    np_arr, _ = convert_df_to_np(test_df)

    normalized_data, ranges, min_values = normalize_data(np_arr)

    assert isinstance(normalized_data, np.ndarray)
    assert isinstance(ranges, np.ndarray)
    assert isinstance(min_values, np.ndarray)
