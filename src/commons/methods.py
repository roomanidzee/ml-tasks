import random
from typing import List

from math import sqrt

from src.commons.classes import Point
from src.commons.types import Float, Integer


def generate_random_points(
        start: Float,
        end: Float,
        limit: Integer
) -> List[Point]:
    """Method for generating random points."""

    return [
        Point(x=random.uniform(start, end), y=random.uniform(start, end))
        for _ in range(limit)
    ]


def get_distance(first: Point, second: Point) -> Float:
    """Get distance between two points"""

    return sqrt(
        (second.x - first.x) ** 2
        +
        (second.y - first.y) ** 2
    )
