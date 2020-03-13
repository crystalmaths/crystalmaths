import angles_from_fft


def test_dotproduct():
    point1 = [1, 2, 3]
    point2 = [4, 5, 6]
    result1 = angles_from_fft.dotproduct(point1, point2)
    assert type(result1) != float, "The calculated dotproduct is in wrong type"
    assert result1 == 32, "The calculation is incorrect"


def test_lengthproduct():
    point1 = [1, 2, 3]
    point2 = [4, 5, 6]
    result2 = angles_from_fft.lengthproduct(point1, point2)
    assert type(result2) == float, "The calculated lengthproduct \
    is in wrong type"
    assert result2 != 0, "At least one of the input point is not acceptable"


def test_angle():
    point1 = [1, 2, 3]
    point2 = [4, 5, 6]
    result3 = angles_from_fft.angle(point1, point2)
    assert result3 < 361, "Calculated angle is greater than 360,\
    which is wrong"
