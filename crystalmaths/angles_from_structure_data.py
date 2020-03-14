import math
import pandas as pd
import numpy as np

def angle_for_all (plane1, plane2, metadata_df):
    """This is the function used to calculate the angle between two planes in miller indices, 
    by calculating arccosine of dot product divide by length product plane1 in format of [h1, k1, l1], 
    plane2 in format of [h2, k2, l2]. lattice_parameter should be written in format of [a, b, c] and alpha, 
    beta, gamma are in degree"""

    


    lattice_parameter, metadata_df['alpha'], metadata_df['beta'], metadata_df['gamma']

    alpha = metadata_df['alpha']*math.pi/180
    beta = metadata_df['beta']*math.pi/180
    gamma = metadata_df['gamma']*math.pi/180
    V_square = ((metadata_df['a']*metadata_df['b']*metadata_df['c'])**2)*(1 + 2*math.cos(alpha)*math.cos(beta)*math.cos(gamma)-math.cos(alpha)**2-math.cos(beta)**2-math.cos(gamma)**2)
    temp = np.zeros((3, 3))
    temp[0][0] = (metadata_df['b']**2*metadata_df['c']**2*math.sin(alpha)**2)/V_square
    temp[0][1] = (metadata_df['a']*metadata_df['b']*metadata_df['c']**2*(math.cos(alpha)*math.cos(beta)-math.cos(gamma)))/V_square
    temp[0][2] = (metadata_df['a']*metadata_df['b']**2*metadata_df['c']*(math.cos(alpha)*math.cos(gamma)-math.cos(beta)))/V_square
    temp[1][0] = (metadata_df['a']*metadata_df['b']*metadata_df['c']**2*(math.cos(alpha)*math.cos(beta)-math.cos(gamma)))/V_square
    temp[1][1] = (metadata_df['a']**2*metadata_df['c']**2*math.sin(beta)**2)/V_square
    temp[1][2] = (metadata_df['a']**2*metadata_df['b']*metadata_df['c']*(math.cos(beta)*math.cos(gamma)-math.cos(alpha)))/V_square
    temp[2][0] = (metadata_df['a']*metadata_df['b']**2*metadata_df['c']*(math.cos(alpha)*math.cos(gamma)-math.cos(beta)))/V_square
    temp[2][1] = (metadata_df['a']**2*metadata_df['b']*metadata_df['c']*(math.cos(beta)*math.cos(gamma)-math.cos(alpha)))/V_square
    temp[2][2] = (metadata_df['a']**2*metadata_df['b']**2*math.sin(gamma)**2)/V_square
    d1_array = np.zeros(3)
    d2_array = np.zeros(3)
    for i in range(3):
        for j in range(3):
            d1_array[i] = d1_array[i]+plane1[j]*temp[j][i]
    for i in range(3):
        for j in range(3):
            d2_array[i] = d2_array[i]+plane2[j]*temp[j][i]
    d1_value = 0
    d2_value = 0
    for i in range(3):
        d1_value = d1_value+d1_array[i]*plane1[i]
    for i in range(3):
        d2_value = d2_value+d2_array[i]*plane2[i]

    numerator_array = np.zeros(3)
    numerator = 0
    for i in range(3):
        for j in range(3):
            numerator_array[i] = numerator_array[i]+plane1[j]*temp[j][i]
    for i in range(3):
        numerator = numerator+numerator_array[i]*plane2[i]
    demoninator = math.sqrt(d1_value*d2_value)
    rad = math.acos(numerator/demoninator)
    degree = 180*rad/math.pi
    return degree

