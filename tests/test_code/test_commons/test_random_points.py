from code import commons


def test_random_generation(prepared_fixed_points):
    assert prepared_fixed_points == commons.generate_random_points(1.0, 1.0, 10)
