import distance_from_fft


def test_dis_cal():
    point = [1, 2]
    ratio = 2
    result1 = distance_from_fft.dis_cal(point, ratio)
    assert result1 != float, "The calculated result is in wrong type"
    assert round(result1, 3) == 0.894, "The calcualtion is incorrect"
