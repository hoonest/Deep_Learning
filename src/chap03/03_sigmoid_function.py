import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


if __name__ == "__main__":
    x = np.array([-1.0, 1.0, 2.0])
    y = sigmoid(x)
    print(y)