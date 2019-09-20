import sys
import random
from typing import List
from collections import defaultdict

from code.commons import Point, Integer, Float
from code.k_means.utils import get_distance, get_average_point


def generate_k_points(
        points: List[Point],
        limit: Integer
) -> List[Point]:
    """Generate k random points from there range."""

    first_dim = [item.x for item in points]
    second_dim = [item.y for item in points]

    return [
        Point(
            x=random.uniform(min(first_dim), max(first_dim)),
            y=random.uniform(min(second_dim), max(second_dim))
        )
        for _ in range(limit)
    ]


def assign_points(
        points: List[Point],
        centers: List[Point]
) -> List[Float]:
    """Assign index of center point to existed point"""
    assignments = []

    for point in points:
        shortest = sys.float_info.max
        shortest_index = 0

        for index, center in enumerate(centers):
            calc_distance = get_distance(point, center)

            if calc_distance < shortest:
                shortest = calc_distance
                shortest_index = index

        assignments.append(shortest_index)

    return assignments


def update_centers(
        points: List[Point],
        assignments: List[Float]
) -> List[Point]:
    """Compute center for each assignment"""

    new_centers = defaultdict(list)

    for assignment, point in zip(assignments, points):
        new_centers[assignment].append(point)

    return [
        get_average_point(item)
        for item in list(new_centers.values())
    ]
