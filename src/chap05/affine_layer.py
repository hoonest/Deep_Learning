import numpy as np
from src.chap05.layer_naive import *

class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(np.dot(x, self.W), self.b)
        return out

    def forward2(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b
        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis = 0)
        return dx



X_dot_W = np.array([[0,0,0], [10,10,10]])
B = np.array([[1,2],[3,4],[5,6]])

dot_layer = Affine(X_dot_W, B)
#add_layer = AddLayer()


# 순전파
print('-------------순전파-----------------')
x = np.array([[1,2], [3,4]])
layer1_value = dot_layer.forward(x)
#layer2_value = add_layer.forward(layer1_value, B)
print(x)
print(layer1_value)
#print(layer2_value)



print('-------------역전파-----------------')
# 역전파
dvalue = 1
#ddotv, db = add_layer.backward(dvalue)
ddotx = dot_layer.backward(dvalue)

#print(ddotv, '===' , db )
print(ddotx)

print('-------------검증-----------------')
print(np.dot(np.dot(x, ddotx.T), B))




print('-------------순전파-----------------')
B2 = np.array([1,2,3])
dot_layer2 = Affine(X_dot_W, B2)
x2 = np.array([1,2])
layer1_value = dot_layer2.forward2(x2)
#layer2_value = add_layer.forward(layer1_value, B)
print(x2)
print(layer1_value)
#print(layer2_value)



print('-------------역전파-----------------')
# 역전파
dvalue = 1
#ddotv, db = add_layer.backward(dvalue)
ddotx = dot_layer2.backward(dvalue)

#print(ddotv, '===' , db )
print(ddotx)

print('-------------검증-----------------')
print(np.dot(x2, ddotx.T) +B2)



