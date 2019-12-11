

from src.svm.utils import calculate_radial_basis


def test_calculate_basis(random_arrays):

    result = calculate_radial_basis(
       random_arrays[0],
       random_arrays[1]
    )

    assert result > 0
