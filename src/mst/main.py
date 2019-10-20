import sys
from typing import List

from src.commons.classes import PointStructure, PointsConnection, Point
from src.commons.methods import get_distance
from src.commons.types import Integer

from src.mst import utils


def connect_structures(
        points: List[PointStructure],
        limit: Integer
) -> List[PointsConnection]:
    """Method for points connection"""

    links = []

    for _ in range(0, limit):

        smallest_num = sys.maxsize
        smallest_structure1, smallest_structure2 = PointStructure(0, Point()), PointStructure(0, Point())

        for point1 in points:
            for point2 in points:

                # check for two points
                if limit == 2:
                    connect_condition = (not point1.is_marked) or (not point2.is_marked)
                else:
                    connect_condition = (not point1.is_marked) and point2.is_marked

                p1 = point1.point_data
                p2 = point2.point_data

                if get_distance(p1, p2) < smallest_num and p1.x != p2.x and p1.y != p2.y and connect_condition:
                    smallest_num = get_distance(p1, p2)

                    smallest_structure1.point_id = point1.point_id
                    smallest_structure1.point_data = point1.point_data

                    smallest_structure2.point_id = point2.point_id
                    smallest_structure2.point_data = point2.point_data

        links.append(
            PointsConnection(
                smallest_structure1.point_id,
                smallest_structure2.point_id
            )
        )

        utils.mark_point(points, smallest_structure1.point_id)
        utils.mark_point(points, smallest_structure2.point_id)

    return links


def remove_longest_link(
        points: List[PointStructure],
        links: List[PointsConnection]
) -> List[PointsConnection]:

    max_size = 0
    max_link = None

    source_point = Point()
    target_point = Point()

    for link in links:

        for point in points:

            if point.point_id == link.target_id:
                target_point.x = point.point_data.x
                target_point.y = point.point_data.y

        for point in points:

            if point.point_id == link.source_id:
                source_point.x = point.point_data.x
                source_point.y = point.point_data.y

        distance = get_distance(source_point, target_point)

        if distance > max_size:
            max_size = distance
            max_link = link

    if max_link:
        links.remove(links[links.index(max_link)])

    return links
