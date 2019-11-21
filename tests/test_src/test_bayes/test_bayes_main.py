from src.bayes.utils import load_data
from src.bayes.main import classify


def test_classify(file_path):
    csv_data = load_data(file_path)

    input = [0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1]
    result = classify(input, csv_data)

    assert result == 0.18142313237158084
