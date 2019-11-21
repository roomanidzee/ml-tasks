import functools
from typing import List

from src.bayes.utils import CSV_DATA
from src.commons.types import Integer, Float


def classify(
        input_data: List[Integer],
        csv_data: CSV_DATA
) -> Float:

    symptoms, diseases = csv_data

    assert len(input_data) == len(symptoms), "not enough input data"
    assert all(elem in [0, 1] for elem in input_data), "wrong input data"

    results = []
    exists_prob = sum(elem for elem in input_data if elem == 1) / len(input_data)
    disease_prob = exists_prob * (1 - exists_prob)

    for elem in diseases:
        counter = 0

        for elem1, elem2 in zip(input_data, elem):
            counter += elem1 * elem2

        prob_sum = functools.reduce(lambda a, b: a + b, elem)
        prob_not_disease = prob_sum - counter

        dis_prob = prob_not_disease / prob_sum

        results.append(dis_prob * disease_prob / exists_prob)

    print('Probabilities: {0}'.format(results))

    return max(results)
