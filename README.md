Identify zone axis from a TEM image

##Flow of implementation:

crystalmaths.setimage User provides a high res transmission electron microscope (HRTEM) image.

crystalmaths.setscale sets the scale of the image in pixels to nm - we get this either from the HRTEM image metadata, or from the user directly as an input.

crystalmaths.setstructure sets the symmetry of the crystal, ie cubic - either we can employ a recent package to get this information from the FFT or we can get this from the user as an input.

crystalmaths.fft applies a fast fourier transform (FFT) to the image and stores this image separately.

crystalmaths.plane trained model identifies the atomic planes, or dots in the FFT, and stores them as objects. Requires machine learning - torch package

crystalmaths.df creates an empty crystalmaths DataFrame

crystalmaths.fftdist measures the distance between planes of atoms in each direction (d spacing) from the FFT and adds these distances into the dataframe.

crystalmaths.fftang measures the angles between each plane based on the FFT adds this information to the crystalmaths DataFrame

crystalmaths.calcang calculates the angles between different planes based on the d spacing from crystalmaths.fftdist and the crystal structure provided by crystalmaths.setstructure and adds this information to the crystalmaths DataFrame

crystalmaths.checkcrystal uses the math.isclose (or equivalent) function and checks to see if the experimental and expected angles are close or throws and error because this is not the correct crystal structure. IE the user input cubic and the angles between planes do not match because they have a hexagonal crystal. 

crystalmaths.getd queries an external structural database to find planes with similar d spacing and crystal structure, and loads near mathes into a structure DataFrame

crystalmaths.zone calculates the zone axis for the top 5 predictions by confidence by taking the cross product of two planes and plots each as a potential zone axis for the user to select
