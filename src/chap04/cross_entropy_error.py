import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t*np.log(y + delta) )

if __name__ == '__main__':
    y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
    t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]

    result = cross_entropy_error(np.array(y), np.array(t))
    print(result)
    result = cross_entropy_error(np.array(y2), np.array(t))
    print(result)