import find_matching_angles


def test_find_matching_angles():
    all_angles_fft = [11, 29, 78]
    all_angles_data = [10, 30, 50, 80]
    tolerance = 1
    matching_angles = find_matching_angles(all_angles_fft, all_angles_data,
                                           tolerance)
    for i in range(0, len(matching_angles)):
        assert abs(matching_angles[i][0] - matching_angles[i][1]) <=\
            tolerance, "Wrong pair of angles"
