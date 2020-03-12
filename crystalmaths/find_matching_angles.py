import numpy as np


def find_matching_angles(all_angles_fft, all_angles_data, tolerance):
    """
    This function finds matching angle pairs between a list of angles obtained
    from FFT (usung "angles_from_fft" function) and a list of angles found
    in structure data base (using "angles_from_structure_data" function).
    Inputs are (1) list of angles from FFT, (2) list of angles from data base,
    (3) value of tolerance to use.
    Output is a list of matching angle pairs.
    """

    matching_angles = []
    for angle_fft in all_angles_fft:
        for angle_data in all_angles_data:
            # check = np.isclose(angle_fft, angle_data, atol=tolerance)
            if np.isclose(angle_fft, angle_data, atol=tolerance) == 1:
                close_pair = [angle_fft, angle_data]
                matching_angles.append(close_pair)
            else:
                pass
    return matching_angles
