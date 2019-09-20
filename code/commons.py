import random

from typing import TypeVar, List
from dataclasses import dataclass

Integer = TypeVar('Integer', int, int)
Float = TypeVar('Float', float, float)


@dataclass
class Point:
    x: Float = 0.0
    y: Float = 0.0


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
