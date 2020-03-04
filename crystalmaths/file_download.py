def file_download(google_shareable_link, output_filename, output_directory):
    """
    This function downloads a file from Google Drive and stores it in a local directory.
    Inputs for the function are: 
    (1) "Shareable link" from Google Drive provided as a string. 
        Example: google_shareable_link = 'https://drive.google.com/open?id=1cFi0rOqN8bcJ7H5fpfPAGS5Rem7TtiII'
        ***To get the link: go to the file in your Google Drive, right click, select "Get Shareable link".
    (2) Output file name including file extension provided as a string. 
        Example: output_filename = 'Hexagonal_18.bmp'
    (3) Output Directory path provided as a string.
        Example: output_directory = '/Users/elenashoushpanova/Desktop/'
    Output for the function is a file path of saved file.
        Example: dir_file = '/Users/elenashoushpanova/Desktop/Hexagonal_18.bmp'
        
    Note: this function calls for a "google_authorization" function.
    """
    
    import io
    from googleapiclient.http import MediaIoBaseDownload
    import skimage
    import skimage.io as sio
    import matplotlib.pyplot as plt
    
    # Call for a google authorization function to get Google Credentials:
    creds = google_authorization() ############ Will need a name change to "crystalmath."
    
    # Define Google Drive as a source of file:
    DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http())) 
    
    # Converts Google Shareable link that function got in Inpout into "file id":
    loc = google_shareable_link.find('id=')+3
    file_id = google_shareable_link[loc:]
    
    # Access a file:
    request = DRIVE.files().get_media(fileId=file_id)
    
    # Merging output directory and file name to get a local file path:
    if output_directory[-1] == '/':
        dir_file = output_directory+output_filename
    else:
        dir_file = output_directory+'/'+output_filename
    
    # Saving a file: 
    fh = io.FileIO(dir_file, mode='w')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    return dir_file

