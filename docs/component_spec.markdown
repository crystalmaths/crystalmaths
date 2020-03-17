
### 1. human machine interface: the human machine interface is used to specify the scale bar and the points on an FFT of thier image which represent planes

Inputs: Scale Bar size in nanometers as an integer input, .bmp or .png image of high res TEM, positions of clicks while in the interface which are used to set the scale ratio in the image and the position of planes in the FFT.

Outputs: scale ratio as a float and position of planes as a list of point coordinates

The human machine interface creates an object of the class image and stores data for other functions to retrieve. Human machine interface software is located in imagetools.py

### 2. crystalmaths package of python functions: the crystalmaths package uses the data from the human machine interface to search the American Minerals Society database for potential crystal structures and returns zone axis for structures with planes that have matching d spacing and angles between planes. Components are listed below

Inputs: scale ratio as a float from the human machine interface, postions of planes in FFT as integers in a list of x y coordinates

Output: A dataframe of potential planes and zone axis

The crystalmaths package calculates the zone axis of a high res TEM image  


crystalmaths.distance_from_fft measures the distance between planes of atoms in each direction (d spacing) from the FFT and adds these distances into the dataframe.
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components

crystalmaths.angles_from_fft measures the angles between each plane based on the FFT adds this information to the crystalmaths DataFrame
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components

crystalmaths.angles_from_structure_data calculates the angles between different planes based on the d spacing from crystalmaths.fftdist and the crystal structure provided by crystalmaths.setstructure and adds this information to the crystalmaths DataFrame
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components

crystalmaths.temp_angles_from_structure_data

crystalmaths.get_d queries an external structural database to find planes with similar d spacing and crystal structure, and loads near mathes into a structure DataFrame
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components

crystalmaths.find_matching_angles uses the math.isclose (or equivalent) function and checks to see if the experimental and expected angles are close or throws and error because this is not the correct crystal structure. IE the user input cubic and the angles between planes do not match because they have a hexagonal crystal.
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components

crystalmaths.compile_results calculates the zone axis for the top 5 predictions by confidence by taking the cross product of two planes and plots each as a potential zone axis for the user to select
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components

crystalmaths.file_download

crystalmaths.google_authorization

crystalmaths.trans_mode
