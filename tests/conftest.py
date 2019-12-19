import random

import pytest
import pandas as pd
import numpy as np

from src.commons.classes import Point


@pytest.fixture
def prepared_fixed_points():
    return [
        Point(x=1.0, y=1.0)
        for _ in range(10)
    ]


@pytest.fixture
def prepared_random_points():
    return [
        Point(x=random.uniform(1.0, 10.0), y=random.uniform(1.0, 10.0))
        for _ in range(10)
    ]


@pytest.fixture
def test_df():
    data = [
        {
            'x': random.uniform(1.0, 10.0),
            'y': random.uniform(1.0, 10.0),
            'label': random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
        }
        for _ in range(100_000)
    ]

    return pd.DataFrame(data)


@pytest.fixture
def test_numpy_arrays(test_df):

    limit = 5

    lists = [
        [
            [
                random.choice(list(range(limit))),
                random.choice(list(range(limit)))
            ]
            for _ in range(limit)
        ],
        [
            [
                random.choice(list(range(limit))),
                random.choice(list(range(limit)))
            ]
            for _ in range(limit)
        ]
    ]

    return np.array(lists[0]), np.array(lists[1])
