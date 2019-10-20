import pytest

from src.mst.utils import create_point_structure


@pytest.fixture
def prepared_structures(prepared_random_points):
    return create_point_structure(prepared_random_points)
