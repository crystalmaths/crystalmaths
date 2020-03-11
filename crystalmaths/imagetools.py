import skimage
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft2, fftshift, ifft
from skimage import img_as_float
from skimage.color import rgb2gray
from skimage import io
import skimage


def setimage(google_shareable_link, output_filename, output_directory):
    """
    This function is similar to "show_image", but it loads image from a\\
     Google Drive instead of local directory.
    Inputs for the function are:
    (1) "Shareable link" from Google Drive provided as a string.
        Example: google_shareable_link =
        'https://drive.google.com/open?id=1cFi0rOqN8bcJ7H5fpfPAGS5Rem7TtiII'
        ***To get the link: go to the file in your Google Drive, right click,\\
        select "Get Shareable link".
    (2) Output file name including file extension provided as a string.
        Example: output_filename = 'Hexagonal_18.bmp'
    (3) Output Directory path provided as a string.
        Example: output_directory = '/Users/elenashoushpanova/Desktop/'
    Output is an array of image pixel values, image pixel resolution, as well\\
        as the image itself.

    Note: this function call for "file_download" and "show_image" functions.
    """
    # Call for a "file_download" function: ############ Will need a name \\
    # change to "crystalmath."
    dir_file = file_download(google_shareable_link, output_filename,
                             output_directory)

    # Call for a "show_image" function: ############ Will need a name change\\
    #  to "crystalmath."
    image = show_image(dir_file)
    return image, image.shape


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


class ImageHandler():
    """
    Class which takes as input an image filepath, turns it into an array, and
    processes the FFT. Methods include get_planes, get_ratio.
    """
    def __init__(self, image_filepath):
        self.image_filepath = image_filepath
        self.image_array = skimage.io.imread(self.image_filepath)
        image_fft = np.abs(np.fft.fftshift((np.fft.fft2(self.image_array))))
        self.image_fft_array = np.log(image_fft)

    def show_image(self):
        fig, axes = plt.subplots(1, 2, figsize=(16, 16))
        axes[0].imshow(self.image_array, cmap='binary_r')
        axes[0].set_title('Loaded Image')
        axes[1].imshow(self.image_fft, cmap='binary_r')
        axes[1].set_title('Image FFT')
        plt.axis('off')

    def get_planes(self):
        prompt = 'Pick planes using left mouse button. Right click once done.\
 Middle mouse button removes most recent point.'
        message = "Press keyboard button to save points, mouseclick to restart"
        print(prompt)
        fig, ax = plt.subplots()
        plt.setp(plt.gca(), autoscale_on=True)
        ax.imshow(self.image_fft, cmap='binary_r')
        # zoom = False
        # while zoom is not True:
        while True:
            plt.title('Perform zoom if necessary, keyboard press to advance')
            if plt.waitforbuttonpress(timeout=-1):
                # zoom = True
                break
        print("Exited zoom loop")
        while True:
            plt.title(prompt, wrap=True)
            fig.canvas.draw()
            while True:
                print("Entered point pick loop")
                points = plt.ginput(n=-1, show_clicks=True, timeout=-1,
                                    mouse_add=1, mouse_stop=3, mouse_pop=2)
                break
            plt.title(message, wrap=True)
            fig.canvas.draw()
            print("Saved points = ", points)
            print(message)
            point_list = []
            if plt.waitforbuttonpress():
                for i in range(len(points)):
                    point_col = int(points[i][0])
                    point_row = int(points[i][1])
                    point_list.append([point_col, point_row])
                self.point_coordinates = point_list
                plt.close()
                break
