
from src.knn.utils import convert_df_to_np
from src.knn.main import classify


def test_knn(test_df):

    np_arr, labels = convert_df_to_np(test_df)
    input_data = [1.0, 3.0]
    k = 2

    result = classify(input_data, np_arr, labels, k)

    assert isinstance(result, str)