from src.commons.methods import generate_random_points, get_distance


def test_random_generation(prepared_fixed_points):
    assert prepared_fixed_points == generate_random_points(1.0, 1.0, 10)


def test_distance(prepared_fixed_points):
    assert get_distance(prepared_fixed_points[0], prepared_fixed_points[1]) == 0.0
