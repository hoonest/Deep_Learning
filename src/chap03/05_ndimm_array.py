import numpy as np

# 1차원 배열(벡터)
A = np.array([1, 2, 3, 4])
print(A)
print(np.ndim(A))
print(A.shape)
print(A.shape[0])


# 2차원 배열(행렬 / matrix)
B = np.array([[1, 2],[3, 4],[5, 6]])
print(B)
print(np.ndim(B))     # 2
print(B.shape)        # (3, 2)


# 행렬의 내적(행렬 곱)
# 2 x 2 행렬
A = np.array([[1, 2], [3, 4]])
print(A.shape)      # (2, 2)

B = np.array([[5, 6], [7, 8]])
print(B.shape)      # (2, 2)

print(np.dot(A, B))  # array([[19, 22],
                     #        [43, 50]])

# 2 x 3 행렬과  3 x 2 행렬의 내적
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.shape) # (2, 3)
B = np.array([[1, 2], [3, 4], [5, 6]])
print(B.shape) # (3, 2)
Z = np.dot(A, B)
print(Z)    # [[22, 28],[49, 64]]

Z = np.dot(B, A)
print(Z)    # [[ 9,12,15],[19,26,33],[29,40,51]]

C = np.array([[1, 2],[3, 4]]) # (2, 2)
# np.dot(A,C)  # error

# A가 2차원 행렬, B가 1차원 배열 곱
A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([7, 8])
print(np.dot(A,B)) # [23 53 83]

# 신경망의 내적(pdf-15p)
X = np.array([1, 2])  # x1 = 1, x2 = 2
W = np.array([[1, 3, 5],[2, 4, 6]])
Y = np.dot(X,W) # [ 5,11,17]
print(Y)




