
### 1. Human machine interface: the human machine interface is used to specify the scale bar and the points on an FFT of thier image which represent planes

**Inputs**: Scale Bar size in nanometers as an integer input, .bmp or .png image of high res TEM, positions of clicks while in the interface which are used to set the scale ratio in the image and the position of planes in the FFT.
**Outputs**: scale ratio as a float and position of planes as a list of point coordinates.

The human machine interface creates an object of the class image and stores data for other functions to retrieve. Human machine interface software is located in imagetools.py.


### 2. Crystalmaths package: the crystalmaths package uses the data from the human machine interface to search the American Minerals Society database for potential crystal structures and returns zone axis for structures with planes that have matching d spacing and angles between these planes. Components are listed below.

**Inputs**: scale ratio as a float from the human machine interface, postions of planes in FFT as integers in a list of x y coordinates.
**Output**: A dataframe of potential planes and zone axis.

The crystalmaths package calculates the zone axis of a high res TEM image in crystalmaths.compile_results.


**2.a crystalmaths.distance_from_fft** measures the distance between planes of atoms in each direction (d spacing) from the FFT and adds these distances into the dataframe.

* **Inputs**: postions of planes in FFT as integers in a list of x y coordinates, scale ratio (pixel/nm) as a float from the human machine interface, image shape (image width in pixels, assuming square image).
* **Output**: distance from the origin (center of the FFT image) to the plane (point) in the FFT image.

crystalmaths.distance_from_fft is being called inside crystalmaths.compile_results function.
Output from crystalmaths.distance_from_fft will be used in crystalmaths.get_d module.


**2.b crystalmaths.angles_from_fft** measures the angles between each plane based on the FFT and adds this information to the crystalmaths DataFrame.

* **Inputs**: postions of planes in FFT as integers in a list of x y coordinates.
* **Outputs** angle in degrees between two planes.

crystalmaths.angles_from_fft is being called inside crystalmaths.compile_results function.
Output from crystalmaths.angles_from_fft will be used in crystalmaths.find_matching_angles.


**2.c crystalmaths.get_d** module that queries an external structural database to find planes with similar d spacing and crystal structure, and loads near mathes into a structure DataFrame.

* **Inputs**: d spacings from FFT as two integers, and a tolerance for search as a float (in Angstrom).
* **Outputs**: a data frame ("data") that contains a list of possible matches of planes (with hkl indices) from American Minerals Society database, with corresponding d spacing within a specified tolerance, and a separate data frame of "metadata" that contains crystal srructure information (crystal name, lattice parameters and angles).

crystalmaths.get_d is being called inside crystalmaths.compile_results function.
Output from crystalmaths.get_d will be used in crystalmaths.angles_from_structure_data.


**2.d crystalmaths.angles_from_structure_data** calculates the angles between each two planes for all possible matching planes form American Minerals Society database, and adds this information to the crystalmaths DataFrame.

* **Inputs**: two data frames "data" and "metadata" obtained from crystalmaths.get_d.
* **Output**: "results" DataFrame that stores pairs of planes (with hkl indices) from American Minerals Society database and angles for each pair of planes.

crystalmaths.angles_from_structure_data is being called inside crystalmaths.compile_results function.
Output from crystalmaths.angles_from_structure_data will be used in crystalmaths.find_matching_angles.


**2.e crystalmaths.find_matching_angles** uses the math.isclose (or equivalent) function and checks to see if the experimental and expected angles are close or throws and error because this is not the correct crystal structure. IE the user input cubic and the angles between planes do not match because they have a hexagonal crystal. In case angles are matched, zone axis is calculated as a cross product between two planes.

* **Inputs**: "results" DataFrame that stores pairs of planes (with hkl indices) from American Minerals Society database and angles between each pair of planes, an angle from FFT, and a tolerance for angles comparison.
* **Output**: "results" DataFrame updated with angle from FFT and whether it matches the angle from structure data base or not within specified tolerance. In case angles are matched, zone axis will be added to a data frame as well.

crystalmaths.find_matching_angles is being called inside crystalmaths.compile_results function.
Output from crystalmaths.find_matching_angles will be modified inside crystalmaths.compile_results function to add a crystal name to "results" data frame for matched pairs of angles.


**2.f crystalmaths.compile_results** a wrapper function that takes inputs from "Human machine interface" and calculates the zone axis for the top 5 predictions by confidence by taking the cross product of two planes and plots each as a potential zone axis for the user to select.

* **Inputs**: image object (updated with user inputs for scale ratio and points at FFT), d spacing tolerance, angle calculation tolerance.
* **Output**: "results" DataFrame updated with angle from FFT and whether it matches the angle from structure data base or not within specified tolerance. In case angles are matched, zone axis will be added to a data frame as well.

crystalmaths.compile_results calls for functions/modules 2.a-2.e.
Output from crystalmaths.compile_results is the final output of crystalmaths.


**2.g crystalmaths.google_authorization** enables users to set up an interface with a google drive.

* **Input**: none
* **Output**: Google Autorization webpage link.

crystalmaths.google_authorization leads user to a Google authorization webpage, where user has to input his cridentials. Once authorized, user will be requested to copy a key password from a webpage and enter it into a dedicated window in a jupyter notebook. Detailed instructions wil be provided. Once done, user is set to use his Google Drive as a source for images.
crystalmaths.google_authorization is used in crystalmaths.file_download.


**2.h crystalmaths.file_download** downloads a file from a specified Google drive to a local filepath.
* **Inputs**: google_shareable_link, output_filename, output_directory.
* **Output**: a local filepath for downloaded image.

crystalmaths.file_download can be used to set image_filepath.


**2.i crystalmaths.trans_mode** transforms a hexagonal miller indices from four components to three components.

* **Input**: hexagonal index as a vector (list of values).
* **Output**: cubic index as a vector.

crystalmaths.trans_mode can be called whenever transfromation of indices is needed.
