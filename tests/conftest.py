import random

import pytest
import pandas as pd

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
