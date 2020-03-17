import numpy as np
import pandas as pd


def find_matching_angles(angle_fft, result_df, tolerance):
    """
    This function finds matching angle pairs between an angle obtained
    from FFT (usung "angles_from_fft" function) and a list of angles found
    in structure data base (using "angles_from_structure_data" function).
    Inputs are (1) a value of angle from FFT, (2) Pandas DataFrame that
    has angles from structure data (obtained using AllAnglePairs class),
    (3) a value of tolerance to use.
    Output is a list of matching angle pairs.
    """
    dummy_array = np.ones(result_df.shape[0])
    dummy_array *= angle_fft
    result_df['angle-fft'] = dummy_array
    check_list = []
    cross_product_list = []
    for i, row in result_df.iterrows():
        angle_data = row['angle']
        if np.isclose(angle_fft, angle_data, atol=tolerance) == 1:
            check_list.append(True)
            plane1 = np.array([row['H1'], row['K1'], row['L1']])
            plane2 = np.array([row['H2'], row['K2'], row['L2']])
            cross_product = np.cross(plane1, plane2)
            cross_product = [int(i) for i in cross_product]
            cross_gcd = np.gcd.reduce(cross_product)
            cross_product = cross_product/cross_gcd
            cross_product_list.append(cross_product)

        else:
            check_list.append(False)
            cross_product_list.append(None)
    result_df['angle match'] = check_list
    result_df['zone axis'] = cross_product_list
    return result_df
