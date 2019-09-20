from typing import List
from math import sqrt

from code.commons import Point, Float


def get_average_point(points: List[Point]) -> Point:
    """Get average point from points input"""

    points_count = float(len(points))

    first_dim = sum([item.x for item in points])
    second_dim = sum([item.y for item in points])

    return Point(x=first_dim / points_count, y=second_dim / points_count)


def get_distance(first: Point, second: Point) -> Float:
    """Get distance between two points"""

    return sqrt(
        (second.x - first.x) ** 2
        +
        (second.y - first.y) ** 2
    )
