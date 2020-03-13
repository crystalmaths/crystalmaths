import angles_from_structure_data


def test_angle_for_all():
    plane1 = [1, 0, 0]
    plane2 = [1, 0, 1]
    lattice_parameter = [3.2093, 3.2093, 5.2103]
    alpha_degree = 90
    beta_degree = 90
    gamma_degree = 120
    result1 = angles_from_structure_data.angle_for_all(
        plane1, plane2, lattice_parameter,
        alpha_degree, beta_degree, gamma_degree
    )
    assert type(result1) == float, "The calculated degree is in wrong type"
    assert result1 < 361, "The calculated degree is greater \
    than 360, not acceptable"
    assert round(result1, 3) == 28.077, "The calculation is incorrect"
