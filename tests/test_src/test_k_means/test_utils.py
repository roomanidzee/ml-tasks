from src.commons.classes import Point
from src.k_means.utils import get_average_point


def test_average(prepared_fixed_points):
    assert get_average_point(prepared_fixed_points) == Point(x=1.0, y=1.0)

