import math
import numpy as np


def hexag_trans(vector):
    '''This is a function used to translate hexagonal lattice\
    with four coordinates to three coordinates. Vector should\
    be written in numpy.array format with four parameters'''
    after = np.zeros(3)
    after[0] = vector[0]-vector[2]
    after[1] = vector[1]-vector[2]
    after[2] = vector[3]
    return after


def angle_to_degree(alpha1, beta1, gamma1):
    '''This is a function used to translate angle from rad to\
    degree, user can obtain degree directly from the function'''
    alpha = alpha1*180/math.pi
    beta = beta1*180/math.pi
    gamma = gamma1*180/math.pi
    print(alpha)
    print(beta)
    print(gamma)
    return alpha, beta, gamma


def trans_to_hexg(vector):
    '''This is a function used to translate vectors with three\
    coordinates to hexagonal coordinates, which has four coordinates'''
    after = np.zeros(4)
    after[0] = (2*vector[0]-vector[1])/3
    after[1] = (2*vector[1]-vector[0])/3
    after[2] = -(vector[0]+vector[1])/3
    after[3] = vector[2]
    return after
