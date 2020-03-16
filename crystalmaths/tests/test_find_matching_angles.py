import find_matching_angles
import numpy as np
import pandas as pd


def test_find_matching_angles():
    """
    This is a test function for "find_matching_angles" function.
    """

    # Creating a "fake" angle from FFT:
    angle_fft = 35

    # Creating a "fake" data table to simulate results from
    # "AllAnglePairs", which has angles ffrom structure data base and
    # corresponding pairs of HKL planes:
    H1 = np.array([1, 1, 1])
    K1 = np.array([0, 1, 1])
    L1 = np.array([0, 0, 1])
    H2 = np.array([1, 1, 1])
    K2 = np.array([1, 1, 0])
    L2 = np.array([0, 1, 0])
    angles = np.array([45, 35.264, 54.736])
    angles_sd_df = pd.DataFrame()
    angles_sd_df['H1'] = H1
    angles_sd_df['K1'] = K1
    angles_sd_df['L1'] = L1
    angles_sd_df['H2'] = H2
    angles_sd_df['K2'] = K2
    angles_sd_df['L2'] = L2
    angles_sd_df['angle'] = angles

    # Specifying tolerance:
    tolerance = 1

    # Calling for a function
    final_results = find_matching_angles.find_matching_angles(angle_fft,
                                                              angles_sd_df,
                                                              tolerance)

    for i in range(0, final_results.shape[0]):
        if abs(final_results['angle'][i] -
               final_results['angle-fft'][i]) <= tolerance:
            assert final_results['angle match'][i] == 1, "Wrong matching"
        else:
            assert final_results['angle match'][i] == 0, "Wrong matching"
