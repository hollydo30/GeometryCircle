"""
COMP 614
Homework 1: Circles
"""

import math
import comp614_module1 as circles


def distance(point0x, point0y, point1x, point1y):
    """
    Given the x- and y-coordinates of two points, computes and returns the 
    distance between them.
    
    Inputs:
    point0x - x-coordinate of point 1 
    point0y - y-coordinate of point 1 
    point1x - x-coordinate of point 2 
    point1y - y-coordinate of point 2 
    
    Output:
    distance_val - value of distance between point 1 and point 2
    """
    
    distance_val = math.sqrt( ((point1y - point0y)**2) + ((point1x - point0x)**2) )
    return distance_val


def midpoint(point0x, point0y, point1x, point1y):
    """
    Given the x- and y-coordinates of two points, computes and returns the
    midpoint of the line segment between them.
    
    Inputs:
    point0x - x-coordinate of point 1 
    point0y - y-coordinate of point 1 
    point1x - x-coordinate of point 2 
    point1y - y-coordinate of point 2 
    
    Output:
    x_m - x-coordinate of midpoint  
    y_m - y-coordinate of midpoint
    """
    
    x_m = (point0x + point1x)/2
    y_m = (point0y + point1y)/2
    return x_m, y_m


def slope(point0x, point0y, point1x, point1y):
    """
    Given the x- and y-coordinates of two points, computes and returns the
    slope of the line segment from (point0x, point0y) to (point1x, point1y).
    
    Inputs:
    point0x - x-coordinate of point 1 
    point0y - y-coordinate of point 1 
    point1x - x-coordinate of point 2 
    point1y - y-coordinate of point 2 
    
    Output:
    slope_val - slope of the line segment from (point0x, point0y) to (point1x, point1y)
    """
    
    slope_val = (point1y - point0y) / (point1x - point0x)
    return slope_val


def perp(lineslope):
    """
    Given the slope of a line, computes and returns the slope of a line 
    perpendicular to the input slope.
    
    Inputs:
    lineslope - slope of a line
    
    Output:
    perp_slope - slope of a line perpendicular to the line whose slope is the input
    """
    
    perp_slope = (-1)/lineslope
    return perp_slope


def intersect(slope0, point0x, point0y, slope1, point1x, point1y):
    """
    Given two lines, where each is represented by its slope and a point
    that it passes through, computes and returns the intersection point
    of the two lines. 
     
    Inputs:
    slope0  - slope through point 1
    point0x - x-coordinate of point 1 
    point0y - y-coordinate of point 1 
    slope1  - slope through point 2
    point1x - x-coordinate of point 2 
    point1y - y-coordinate of point 2 
    
    Output:
    x_intersect, y_intersect - a tuple of x-coordinate and y-coordinate of the intersect 
    """
    
    # Use these formulars x = (b1-b0) / (m0-m1), b0 = -m0*x0+y0, b1 = -m1*x1+y1
    # x= (-(m0*x0)+y0 - ((-m1*x1)+y1)) / (m0-m1) 
    b2_b1 = -(slope1*point1x) + point1y + (slope0*point0x) - point0y
    x_intersect = b2_b1 / (slope0 - slope1)
    y_intersect = slope0 * (x_intersect - point0x) + point0y
    return x_intersect, y_intersect


def make_circle(point0x, point0y, point1x, point1y, point2x, point2y):
    """
    Given the x- and y-coordinates of three points, computes and returns
    three real numbers: the x- and y-coordinates of the center of the circle
    that passes through all three input points, and the radius of that circle.
    
    Inputs:
    point0x - x-coordinate of point 1 
    point0y - y-coordinate of point 1
    point1x - x-coordinate of point 2 
    point1y - y-coordinate of point 2 
    point2x - x-coordinate of point 3 
    point2y - y-coordinate of point 3 
    
    Intermediate values to be used as inputs to another function:
    slope0  - slope of line segment through (point0x, point0y) and (point1x, point1y)
    slope1  - slope of line segment through (point1x, point2y) and (point2x, point2y)
    x_m0,y_m0 - midpoint between (point0x, point0y) and (point1x, point1y)
    x_m1,y_m1 - midpoint between (point0x, point0y) and (point2x, point2y)
    
    Output:
    x_intersect, y_intersect - a tuple of x-coordinate and y-coordinate of the intersect 
    radius - length of the radius of that circle
    """
    
    x_m0,y_m0 = midpoint(point0x, point0y, point1x, point1y)
    x_m1,y_m1 = midpoint(point0x, point0y, point2x, point2y)
    slope0 = perp(slope(point0x, point0y, point1x, point1y))
    slope1 = perp(slope(point0x, point0y, point2x, point2y))
    x_intersect, y_intersect = intersect(slope0, x_m0, y_m0, slope1, x_m1, y_m1)
    radius = distance(x_intersect, y_intersect, point1x, point1y)
    return x_intersect, y_intersect, radius


    
# Run GUI - uncomment the line below after you have
#           implemented make_circle
#circles.start(make_circle)