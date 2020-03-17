
### 1. human machine interface: the human machine interface is used to specify the scale bar and the points on an FFT of thier image which represent planes

Inputs: Scale Bar size in nanometers as an integer input, .bmp or .png image of high res TEM, positions of clicks while in the interface which are used to set the scale ratio in the image and the position of planes in the FFT.

Outputs: scale ratio as a float and position of planes as a list of point coordinates

The human machine interface creates an object of the class image and stores data for other functions to retrieve. Human machine interface software is located in imagetools.py

### 2. crystalmaths package of python functions: the crystalmaths package uses the data from the human machine interface to search the American Minerals Society database for potential crystal structures and returns zone axis for structures with planes that have matching d spacing and angles between planes. Components are listed below

Inputs: scale ratio as a float from the human machine interface, postions of planes in FFT as integers in a list of x y coordinates

Output: A dataframe of potential planes and zone axis

The crystalmaths package calculates the zone axis of a high res TEM image  


2.a crystalmaths.distance_from_fft measures the distance between planes of atoms in each direction (d spacing) from the FFT and adds these distances into the dataframe.
* Inputs ([point1, point2], )
* Outputs (with type information)
* How it interacts with other components

2.b crystalmaths.angles_from_fft measures the angles between each plane based on the FFT adds this information to the crystalmaths DataFrame
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components

2.c crystalmaths.angles_from_structure_data calculates the angles between different planes based on the d spacing from crystalmaths.fftdist and the crystal structure provided by crystalmaths.setstructure and adds this information to the crystalmaths DataFrame
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components

2.d crystalmaths.temp_angles_from_structure_data_Edwin
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components

2.e crystalmaths.get_d queries an external structural database to find planes with similar d spacing and crystal structure, and loads near mathes into a structure DataFrame
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components

2.f crystalmaths.find_matching_angles uses the math.isclose (or equivalent) function and checks to see if the experimental and expected angles are close or throws and error because this is not the correct crystal structure. IE the user input cubic and the angles between planes do not match because they have a hexagonal crystal.
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components

2.g crystalmaths.compile_results calculates the zone axis for the top 5 predictions by confidence by taking the cross product of two planes and plots each as a potential zone axis for the user to select
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components

2.h crystalmaths.google_authorization enables users to set up an interface with a google drive.
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components

2.i crystalmaths.file_download downloads a file from a specified good drive to a local filepath.
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components

2.j crystalmaths.trans_mode transforms a hex miller indice from four components to three components
* Inputs (with type information)
* Outputs (with type information)
* How it interacts with other components