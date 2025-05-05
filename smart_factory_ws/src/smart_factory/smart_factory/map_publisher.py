import math
import numpy as np

def angle_calculator(x1,y1,x2,y2,theta):

    theta = theta
    cos = math.cos(theta)
    sin = math.sin(theta)
    # rotation_matrix = np.matrix([[cos,-sin],[sin,cos]])
    
    x1 = x1
    y1 = y1
    
    x2 = x2
    y2 = y2

    # xy_matrix = np.matrix([[x],[y]])

    vect_A = math.hypot((x2-x1),(y2-y1))

    dist_origin = vect_A
    angle_origin = math.degrees(math.atan2((y2-y1),(x2-x1)))

    print(f'distance:{dist_origin}, angle: {angle_origin}')
    
    # new_matrix = rotation_matrix * xy_matrix

    # print(f"After Rotation: {new_matrix}")
    
def main():
    x1 = -2
    y1 = -0.5

    x2 = -1
    y2 = -1.5
    theta = 0
    angle_calculator(x1,y1,x2,y2,theta)

if __name__ == '__main__':
    main()