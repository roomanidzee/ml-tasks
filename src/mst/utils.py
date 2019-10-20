from typing import List

from src.commons.classes import PointStructure, Point
from src.commons.types import Integer


def create_point_structure(
        points: List[Point]
) -> List[PointStructure]:

    return [
        PointStructure(i, points[i], False)
        for i in range(0, len(points))
    ]


def mark_point(
        point_data: List[PointStructure],
        point_id: Integer
) -> None:
    for elem in point_data:
        if elem.point_id == point_id:
            elem.is_marked = True
