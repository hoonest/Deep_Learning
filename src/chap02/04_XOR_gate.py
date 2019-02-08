import numpy as np
# from 02_AND_bias import AND

# AND gate
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

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

# XOR Gate
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)

    return y

if __name__ == "__main__":

    x = XOR(0, 0) # 0
    print(x)
    x = XOR(0, 1) # 1
    print(x)
    x = XOR(1, 0) # 1
    print(x)
    x = XOR(1, 1) # 0
    print(x)

