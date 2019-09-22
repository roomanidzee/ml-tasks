from src.k_means.main import generate_k_points, assign_points, update_centers


def test_k_means(prepared_random_points):
    k_points = generate_k_points(prepared_random_points, 2)
    assignments = assign_points(prepared_random_points, k_points)
    old_assignments = None

    print(f"POINTS: {prepared_random_points}")
    print(f"K_POINTS: {k_points}")
    print(f"ASSIGNMENTS: {assignments}")
    while assignments != old_assignments:
        new_centers = update_centers(prepared_random_points, assignments)
        old_assignments = assignments
        assignments = assign_points(prepared_random_points, new_centers)

    print(f"POINTS: {prepared_random_points}")
    print(f"K_POINTS: {k_points}")
    print(f"ASSIGNMENTS: {assignments}")

    assert len(assignments) == 10
