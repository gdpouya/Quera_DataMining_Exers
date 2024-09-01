# coding: utf-8
import numpy as np
def calc_two_loops(new_points, points):
    
    #‌ m is the number of new points (test samples)
    m = len(new_points)
    # n is the number of points (training samples)
    n = len(points)
    # Distance matrix
    d = np.zeros((m, n))
    
    # For each new point
    for i in range(m):
        # For each point
        for j in range(n):
            t1=np.square(new_points[i][0]-points[j][0])
            t2=np.square(new_points[i][1]-points[j][1])
            t3=np.square(new_points[i][2]-points[j][2])
            t4=np.square(new_points[i][3]-points[j][3])
            
            # Calculate the distance between the two points
            d[i, j] = np.sum([t1,t2,t3,t4]) # TO-DO
            
            
    return d
