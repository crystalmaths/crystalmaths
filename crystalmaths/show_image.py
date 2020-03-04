def show_image(dir_file):
    """
    This function loads image from a local directory.
    Input is an image file path.
    Output is an array of image pixel values, as well as the image itself.
    """
    
    image = sio.imread(dir_file)
    sio.imshow(image)
    plt.axis('off')
    return image

