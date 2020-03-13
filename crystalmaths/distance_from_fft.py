import math


def dis_cal(point, ratio):
    '''This is a function used to calculate the distance\
    between one point and origin. The ratio should be in\
    unit of pixel/nm'''
    cord_list = []
    for i in range(len(point)):
        cord_list.append(point[i]**2)
    dis_calculation = ratio/math.sqrt(sum(cord_list))
    return dis_calculation
