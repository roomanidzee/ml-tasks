import random

import pytest

from code import commons


@pytest.fixture
def prepared_fixed_points():
    return [
        commons.Point(x=1.0, y=1.0)
        for _ in range(10)
    ]


@pytest.fixture
def prepared_random_points():
    return [
        commons.Point(x=random.uniform(1.0, 10.0), y=random.uniform(1.0, 10.0))
        for _ in range(10)
    ]
