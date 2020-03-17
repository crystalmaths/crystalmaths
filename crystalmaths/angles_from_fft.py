import math


def dotproduct(point1, point2):
    """This is the function used to calculate the dot \
    product between two vectors, which will be used as \
    numerator for angle calculation"""
    result = 0
    for i in range(len(point1)):
        result = result + point1[i]*point2[i]
    return result


def lengthproduct(point1, point2):
    """This is the function used to calculate the length \
    of given two vectors and their product, which will be \
    used as denominator for angle calculation"""
    len1 = 0
    len2 = 0
    for i in range(len(point1)):
        len1 = len1 + point1[i]*point1[i]
    for i in range(len(point2)):
        len2 = len2 + point2[i]*point2[i]
    len1 = math.sqrt(len1)
    len2 = math.sqrt(len2)
    lengthproduct = len1*len2
    return lengthproduct


def angle(point1, point2):
    """This is the function used to calculate the angle \
    between two vectors, by calculating arccosine of dot \
    product divide by length product"""
    rad = math.acos(dotproduct(point1, point2)/lengthproduct(point1, point2))
    degree = 180*rad/math.pi
    return degree
