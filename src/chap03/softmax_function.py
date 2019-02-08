import numpy as np
import matplotlib.pylab as plt
'''
a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)
sum_exp_a = np.sum(exp_a)
y = exp_a / sum_exp_a

print(exp_a[0], '/', sum_exp_a, '=', y[0])
print(exp_a[1], '/', sum_exp_a, '=', y[1])
print(exp_a[2], '/', sum_exp_a, '=', y[2])
'''


def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def draw(a,y):
    plt.plot(a,y)
    plt.ylim(-0.1, 1.0)
    plt.show()

if __name__ == '__main__':
    a = np.array([0.3, 2.9, 4.0])
    print(a)
    y = softmax(a)
    print(y)
    draw(a, y)
