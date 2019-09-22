from src.k_means.main import generate_k_points, assign_points, update_centers


def test_generate_k_points(prepared_fixed_points):

    k_points = generate_k_points(prepared_fixed_points, 10)
    assert len(k_points) == 10


def test_assign_points(prepared_fixed_points):

    assignments = assign_points(prepared_fixed_points, prepared_fixed_points)
    assert len(assignments) == 10


def test_update_centers(prepared_fixed_points):

    updated = update_centers(prepared_fixed_points, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    assert len(updated) == 10
