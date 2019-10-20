from src.commons.classes import PointStructure
from src.mst import utils


def test_structure_creation(prepared_fixed_points):

    structures = utils.create_point_structure(prepared_fixed_points)

    assert structures[0] == PointStructure(0, prepared_fixed_points[0], False)


def test_mark_point(prepared_fixed_points):

    structures = utils.create_point_structure(prepared_fixed_points)

    utils.mark_point(structures, 0)

    assert structures[0] == PointStructure(0, prepared_fixed_points[0], True)
