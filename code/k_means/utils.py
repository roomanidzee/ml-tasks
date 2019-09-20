from typing import List
from math import sqrt

from code import commons


def get_average_point(points: List[commons.Point]) -> commons.Point:
    """Get average point from points input"""

    points_count = float(len(points))

    first_dim = sum([item.x for item in points])
    second_dim = sum([item.y for item in points])

    return commons.Point(
        x=first_dim / points_count,
        y=second_dim / points_count
    )


def get_distance(first: commons.Point, second: commons.Point) -> commons.Float:
    """Get distance between two points"""

    return sqrt(
        (second.x - first.x) ** 2
        +
        (second.y - first.y) ** 2
    )
