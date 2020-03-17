def create_summary_df(image_object, d_spacing_tolerance, angle_tolerance,
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
        result_df = find_matching_angles(fft_angle, result_df, angle_tolerance)
        final_df = result_df[result_df['angle match'] == True]
        if final_df.empty:
            pass
        else:
            mineral_name = metadata_df['Mineral_Name'].values
            n = final_df.shape[0]
            mineral_name_list = [mineral_name for i in range(n)]
            final_df.insert(0, 'Mineral_Name', mineral_name_list)
            angle_compare_list.append((final_df, metadata_df))
    return angle_compare_list
