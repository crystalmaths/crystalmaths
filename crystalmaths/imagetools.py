import skimage
import functools
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft2, fftshift, ifft
from skimage import img_as_float
from skimage.color import rgb2gray
from scipy.signal import get_window
from skimage import io
from skimage import transform


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

     If user chooses to apply window_type, window will be calculated based
     on argument provided. New windowed_image_array attribute created.
     The original array is still used for display purposes and identifying
     scalebar. But the image_fft will be of the windowed image instead of
     the original image.

     Todo:
    - create shifted points attribute which shifts the origin of the fft
    """
    def __init__(self, image_filepath, window_type=None, scale_ratio=None):
        self.image_filepath = image_filepath
        self.image_array = skimage.io.imread(self.image_filepath, as_gray=True)
        if window_type is not None:
            window = self.apply_window(window_type)
            self.windowed_image_array = self.image_array*window
            image_fft = np.abs(np.fft.fftshift((np.fft.fft2(
                self.windowed_image_array))))
            self.image_fft_array = np.log(image_fft)
        else:
            image_fft = np.abs(np.fft.fftshift((np.fft.fft2(
                self.image_array))))
            self.image_fft_array = np.log(image_fft)

    def show_image(self):
        fig, axes = plt.subplots(1, 2)
        axes[0].imshow(self.image_array, cmap='binary_r')
        axes[0].set_title('Loaded Image')
        axes[1].imshow(self.image_fft_array, cmap='binary_r')
        axes[1].set_title('Image FFT')
        plt.axis('off')

    def get_scale_ratio(self, scale_ratio=None):
        """
        This function can receive a pixel to nm ratio as its argument, which\
skips over defining the scalebar on the figure. If no ratio is provided,\
prompt is initiated. This will open up the image_array, and prompt user with\
instructions.
        """
        if scale_ratio is not None:
            # assert(type(scale_ratio)==float)
            self.scale_ratio = float(scale_ratio)
        else:
            prompt = 'Define the scalebar position. Pick end points using left\
mouse button. Right click once done. Middle mouse button removes most recent\
point.'
            fig, ax = plt.subplots()
            plt.setp(plt.gca(), autoscale_on=True)
            ax.imshow(self.image_array, cmap='binary_r')
            plt.title(prompt, wrap=True)
            points = []
            length_nm = float(input("Enter scalebar length in nanometers."))

            while len(points) < 2:
                points = np.asarray(plt.ginput(n=2, show_clicks=True,
                                    timeout=-1, mouse_add=1, mouse_stop=3,
                                    mouse_pop=2))
            length_pixel = np.abs(points[0][0]-points[1][0])
            print("length_nm = ", length_nm)
            print("length_pixel =", length_pixel)
            plt.close()
            self.scale_ratio = length_pixel/length_nm

    def get_planes(self):
        prompt = 'Pick two planes using left mouse button. Right click once\
 done. Middle mouse button removes most recent point.'
        message = "Press keyboard button to save points, mouseclick to restart"
        print(prompt)
        fig, ax = plt.subplots()
        plt.setp(plt.gca(), autoscale_on=True)
        ax.imshow(self.image_fft_array, cmap='binary_r')
        # zoom = False
        # while zoom is not True:
        while True:
            plt.title('Perform zoom if necessary, press down arrow key to\
 continue with plane selection', wrap=True)
            if plt.waitforbuttonpress(timeout=-1):
                # zoom = True
                break
        while True:
            plt.title(prompt, wrap=True)
            fig.canvas.draw()
            while True:
                points = plt.ginput(n=2, show_clicks=True, timeout=-1,
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
                raw_point_coordinates = point_list
                # The center of the image is shifted to index 0,0, to ease
                # calculation of angles between points downstream.
                p1, p2 = raw_point_coordinates
                p1[0] = p1[0] - self.image_array.shape[0]/2
                p1[1] = p1[1] - self.image_array.shape[1]/2
                p2[0] = p2[0] - self.image_array.shape[0]/2
                p2[1] = p2[1] - self.image_array.shape[1]/2
                self.point_coordinates = [p1, p2]
                plt.close()
                break

    def apply_window(self, window_type):
        """
        Code taken from scikit-image window function. At time of writing\
        this the window function is only available in scikit-image development\
        build, and decision was made to not require that for this module.

        This is an optional method which can be called at the time of class\
        initialization in order to apply a specified window to the image array\
        before performing FFT. The purpose is to reduce image edge and\
        scalebar artifacts.
        """
        shape = self.image_array.shape
        ndim = len(shape)
        max_size = functools.reduce(max, shape)
        w = get_window(window_type, max_size, fftbins=False)
        w = np.reshape(w, (-1,)+(1,)*(ndim-1))

        # Create coords for warping following `ndimage.map_coordinates`
        # convention.
        L = [np.arange(s, dtype=np.float32) * (max_size / s) for s in shape]

        center = (max_size/2)-0.5
        dist = 0
        for g in np.meshgrid(*L, sparse=True, indexing='ij'):
            g -= center
            dist = dist + g*g
            dist = np.sqrt(dist)
            coords = np.zeros((ndim,)+dist.shape, dtype=np.float32)
            coords[0] = dist + center

        return transform.warp(w, coords, mode='constant')
