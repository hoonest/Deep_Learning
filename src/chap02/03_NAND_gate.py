import numpy as np

# NAND Gate
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    bias = 0.7

    tmp = np.sum(w * x) + bias
    if tmp <= 0:
        return 0
    else:
        return 1

#####################################################

# OR Gate
def OR(x1, x2):
    w = np.array([0.5, 0.5]) # AND와는 모두 같은 구조의 피셉트론
    x = np.array([x1, x2])
    b = -0.2

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1







