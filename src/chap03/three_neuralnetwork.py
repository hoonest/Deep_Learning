# 입력층에서 1층으로 신호 전달

import numpy as np
import matplotlib.pylab as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def step_function(x):
    return np.array(x > 0, dtype=np.int)

def identity_function(x):
    return x


# 1Layer 계산
print('# 1Layer 계산')
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(X.shape), print(W1.shape), print(B1.shape)
print(np.dot(X, W1))
A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)

print(A1)
print(Z1)
print(step_function(A1))
print(identity_function(A1))

plt.plot(A1, Z1)
plt.plot(A1, step_function(A1), 'k--')
plt.plot(A1, identity_function(A1))
plt.ylim(0.1, 1.1)
plt.show()


# 2 Layer계산
print('# 2 Layer계산')
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

print(Z1.shape), print(W2.shape), print(B2.shape)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)
print(A2)
print(Z2)
print(step_function(A2))
print(identity_function(A2))


plt.plot(A2, Z2)
plt.plot(A2, step_function(A2), 'k--')
plt.plot(A2, identity_function(A2))
plt.ylim(0.1, 1.1)
plt.show()

# 3Layer 계산(출력층)
print('# 3Layer 계산(출력층)')
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

print(Z2.shape), print(W3.shape), print(B3.shape)

A3 = np.dot(Z2, W3) + B3
Z3 = identity_function(A3)

print(A3)
print(Z3)
print(step_function(A3))
print(sigmoid(A3))


plt.plot(A3, Z3)
plt.plot(A3, step_function(A3), 'k--')
plt.plot(A3, sigmoid(A3))
plt.ylim(0.1, 1.1)
plt.show()





# 구현 정리
print('# 구현 정리')
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['B1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['B2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['B3'] = np.array([0.1, 0.2])

    return  network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    B1, B2, B3 = network['B1'], network['B2'], network['B3']

    A1 = np.dot(x, W1) + B1
    Z1 = sigmoid(A1)
    A2 = np.dot(Z1, W2) + B2
    Z2 = sigmoid(A2)
    A3 = np.dot(Z2, W3) + B3
    y = identity_function(A3)

    return y


network = init_network()
x = np.array([[1.0, 0.5], [-0.5, 0.2], [0.3, 0.9], [0.8, -0.6]])
y = forward(network, x)
print(y)
plt.plot(x,y)
plt.ylim(0.1, 1)
plt.show()

