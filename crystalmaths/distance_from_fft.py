import math


def distance_from_fft(point, ratio, image_shape):
    '''This is a function used to calculate the distance\
    between one point and origin. The ratio should be in\
    unit of pixel/nm'''
    cord_list = []
    for i in range(len(point)):
        cord_list.append(point[i]**2)
    pixel_length = math.sqrt(sum(cord_list))

    factor = ratio/image_shape
    inverse_length = 1/(factor*pixel_length)*10  # units 1/angstrom
    return inverse_length
