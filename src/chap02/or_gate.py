import numpy as np

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b

    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

if __name__ == '__main__':
    z = [(0,0), (0,1), (1,0), (1,1)]
    for xs in z:
        y = OR(xs[0], xs[1])
        print(str(xs) +' --> ' + str(y))