from src.bayes.utils import load_data


def test_load_data(file_path):
    symptoms, diseases = load_data(file_path)

    assert symptoms[0][1] == 0.96
    assert diseases[0][1] == 0.99
