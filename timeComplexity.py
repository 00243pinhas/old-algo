import math

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Python 

def solution(X, Y, D):

    if X >= Y:
        return 0

    dist_x_y= Y-X
    min_jump= dist_x_y/D 

    return math.ceil(min_jump)