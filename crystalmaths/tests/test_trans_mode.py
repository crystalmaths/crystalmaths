import trans_mode
import numpy as np
import math


def test_hexag_trans():
    vector = [-1, 2, -1, 3]
    result1 = trans_mode.hexag_trans(vector)
    assert len(result1) == 3, "hexag_trans failed to transform \
    vector with four parameters to three parameters"
    assert type(result1) == np.ndarray, "The output data is in wrong type"
    assert result1[0] == 0, "The calculation is wrong"
    assert result1[1] == 3, "The calculation is wrong"


def test_angle_to_degree():
    alpha1 = math.pi
    beta1 = math.pi/2
    gamma1 = math.pi/3
    result2 = trans_mode.angle_to_degree(alpha1, beta1, gamma1)
    assert result2[0] < 361, "Calculated angle is greater than \
    360, which is wrong"
    assert result2[1] < 361, "Calculated angle is greater than \
    360, which is wrong"
    assert result2[2] < 361, "Calculated angle is greater than \
    360, which is wrong"
