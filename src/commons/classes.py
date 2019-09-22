from dataclasses import dataclass

from src.commons.types import Float


@dataclass
class Point:
    x: Float = 0.0
    y: Float = 0.0
