from code.commons import Point
from code.k_means.utils import get_average_point, get_distance


def test_average(prepared_points):
    assert get_average_point(prepared_points) == Point(x=1.0, y=1.0)


def test_distance(prepared_points):
    assert get_distance(prepared_points[0], prepared_points[1]) == 0.0
