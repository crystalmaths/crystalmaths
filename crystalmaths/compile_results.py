import crystalmaths


def compile_results(image_object, d_spacing_tolerance, angle_tolerance,
                    mineral=None):
    """
    get_zone_axis will take one image_object which has had two planes
    selected on it. The two points (e.g. d1, d2) will be passed as
    arguments to get_d, which searches the ACMS online database to
    generate a list of candidate minerals, based on the d-spacing
    of the selected points from fft image.

    Tolerances for search criteria are also passed as float arguments into
    this function to provide cutoffs for difference in d-spacing and in
    angles.

    get_zone_axis returns a DataFrame with the HKL and mineral name
    for all sets of matching planes
    """
    angle_compare_list = []
    p1 = image_object.point_coordinates[0]
    p2 = image_object.point_coordinates[1]
    fft_angle = crystalmaths.angles_from_fft.angle(p1, p2)
    d1 = crystalmaths.distance_from_fft.distance_from_fft(
        p1, image_object.scale_ratio, image_object.image_array.shape[0])
    d2 = crystalmaths.distance_from_fft.distance_from_fft(
        p2, image_object.scale_ratio, image_object.image_array.shape[0])
    link = crystalmaths.get_d.make_web_address(
        d1, d2, tolerance=d_spacing_tolerance, mineral=mineral)
    print("Searching this page:", link)
    link_list = crystalmaths.get_d.compile_links(link)
    query_results = crystalmaths.get_d.get_d(link_list, [d1, d2])
    for i, result in enumerate(query_results):
        data_df = result[0]
        metadata_df = result[1]
        temp_object = crystalmaths.angles_from_structure_data.AllAnglePairs(
            data_df, metadata_df)
        result_df = temp_object.result_df
        result_df = crystalmaths.find_matching_angles.find_matching_angles(
            fft_angle, result_df, angle_tolerance)

        if result_df.empty:
            pass
        elif result_df['angle match'].any():
            final_df = result_df[result_df['angle match']]
            mineral_name = metadata_df['Mineral_Name'].values
            n = final_df.shape[0]
            mineral_name_list = [mineral_name for i in range(n)]
            final_df.insert(0, 'Mineral_Name', mineral_name_list)
            angle_compare_list.append((final_df, metadata_df))
        else:
            pass
    if len(angle_compare_list) is 0:
        print("Search criteria yield no results.")
    return angle_compare_list


def merge_results(result_list):
    for i, result in enumerate(result_list):
        if i == 0:
            summary_df = result[0].copy(deep=True)
            summary_df.reset_index()
        else:
            summary_df = summary_df.append(result[0], ignore_index=True)
    summary_df.drop(columns='angle match', inplace=True)
    summary_df['D1-RESIDUAL'] = summary_df.apply(
        lambda row: (row['D-REF1']-row['D-SPACING1'])**2, axis=1)
    summary_df['D2-RESIDUAL'] = summary_df.apply(
        lambda row: (row['D-REF2']-row['D-SPACING2'])**2, axis=1)
    summary_df['ANGLE-RESIDUAL'] = summary_df.apply(
        lambda row: (row['angle']-row['angle-fft'])**2, axis=1)
    summary_df.sort_values(by='ANGLE-RESIDUAL', inplace=True)
    summary_df.columns = [x.upper() for x in summary_df.columns]
    return summary_df
