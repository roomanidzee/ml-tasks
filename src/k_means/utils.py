from typing import List

from src.commons.classes import Point


def get_average_point(points: List[Point]) -> Point:
    """Get average point from points input"""

    points_count = float(len(points))

    first_dim = sum([item.x for item in points])
    second_dim = sum([item.y for item in points])

    return Point(
        x=first_dim / points_count,
        y=second_dim / points_count
    )