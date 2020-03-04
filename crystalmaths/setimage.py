def setimage(google_shareable_link, output_filename, output_directory):
    """
    This function is similar to "show_image", but it loads image from a Google Drive instead of local directory.
    Inputs for the function are: 
    (1) "Shareable link" from Google Drive provided as a string. 
        Example: google_shareable_link = 'https://drive.google.com/open?id=1cFi0rOqN8bcJ7H5fpfPAGS5Rem7TtiII'
        ***To get the link: go to the file in your Google Drive, right click, select "Get Shareable link".
    (2) Output file name including file extension provided as a string. 
        Example: output_filename = 'Hexagonal_18.bmp'
    (3) Output Directory path provided as a string.
        Example: output_directory = '/Users/elenashoushpanova/Desktop/'
    Output is an array of image pixel values, image pixel resolution, as well as the image itself.
    
    Note: this function call for "file_download" and "show_image" functions.
    """
    
    # Call for a "file_download" function: ############ Will need a name change to "crystalmath."
    dir_file = file_download(google_shareable_link, output_filename, output_directory)
    
    # Call for a "show_image" function: ############ Will need a name change to "crystalmath."
    image = show_image(dir_file)
    return image, image.shape

