import pytest

from code.commons import Point


@pytest.fixture
def prepared_points():
    return [
        Point(x=1.0, y=1.0)
        for i in range(10)
    ]
