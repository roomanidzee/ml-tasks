from dataclasses import dataclass

from src.commons.types import Float, Integer, Boolean


@dataclass
class Point:
    x: Float = 0.0
    y: Float = 0.0


@dataclass
class PointStructure:
    point_id: Integer
    point_data: Point
    is_marked: Boolean = False


@dataclass
class PointsConnection:
    source_id: Integer
    target_id: Integer
