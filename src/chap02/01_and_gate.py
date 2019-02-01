# coding: utf-8
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def and2(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

if __name__ == '__main__':
    z = [(0,0), (1,0), (0,1), (1,1)]
    for xs in z:
        y = AND(xs[0], xs[1])
        print('AND-> ' + str(xs) + "->" + str(y))
        print('-------------')
        y = and2(xs[0], xs[1])
        print('and2-> ' + str(xs) + "->" + str(y))
        print('==============')