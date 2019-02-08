import numpy as np

A = np.array([1, 2, 3, 4])
print(A)
print(np.ndim(A))
print(A.shape)
print(A.shape[0])

B = np.array([[1,2], [3,4], [5,6]])
#B = np.array([[[1,2], [3,4], [5,6]], [[1,2], [3,4], [5,6]], [[1,2], [3,4], [5,6]]])
print(B)
print(np.ndim(B))
print(B.shape)
print(B.shape[0], "===" , B.shape[1])


# 행렬의 내적(행렬의 곱)

A = np.array([[1,2], [3,4]])
print(A.shape)
B = np.array([[5, 6], [7, 8]])
print(B.shape)
print(np.dot(A,B))

# 2x3행렬과 3x2행렬의 내적

A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.shape)
B = np.array([[1,2], [3, 4], [5, 6]])
print(B.shape)

print(np.dot(A, B))

print(np.dot(B, A))


C = np.array([7,8])
print(C.shape)
print(np.dot(B,C))



# 신경망의 내적

X = np.array([1, 2]) # x1=1, x2=2
W = np.array([[1, 3, 5], [2, 4, 6]])
Y = np.dot(X, W)
print(Y)




