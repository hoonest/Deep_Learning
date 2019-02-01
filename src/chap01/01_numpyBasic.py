# 배열 or 행렬 계산 - Numpy(Numerical Python : 과학적 계산(선형대수)

import numpy as np

# 1. 배열 생성
x = np.array([1.0, 2.0, 3.0])
print(x)                        # [1. 2. 3.]
print(type(x))                  # <class 'numpy.ndarray'>
print(x.shape)                  # (3,)
print(x[0], x[1], x[2])         # 1.0 2.0 3.0
x[2] = 50
print(x)                        # [ 1.  2. 50.]


print('###### 2 #####')
# 2. 산술 연산
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
# 연산시 배열의 자릿수가 동일해야 한다  x = np.array([1.0, 2.0, 3.0, 4.0]) 이면 아래 에러 발생
print(x + y)                    # [3. 6. 9.]
print(x - y)                    # [-1. -2. -3.]
print(x * y)                    # [ 2.  8. 18.]
print(x / y)                    # [0.5 0.5 0.5]

print(x / 2.0)                  # [0.5 1.  1.5]


print('###### 3 #####')
# 3. N차원 배열
# B = np.array([1,2, 3], [4, 5, 6]) # 오류 발생 : TypeError: data type not understood -> [[],[]]
A = np.array([[1,2, 3], [4, 5, 6]])
print(A)                            # [[1 2 3]
                                    #  [4 5 6]]
print(A.shape)                      # (2, 3)
print(A.dtype)                      # int32
print(A[0][1])                      # 2에 접근하기 numpy에서 두가지 방법 허용
print(A[0, 1])                      # 2에 접근하기
print(A[1][0])                      # 4에 접근하기 numpy에서 두가지 방법 허용
print(A[1, 0])                      # 4에 접근하기

B = np.array([[3, 0, 1], [0, 6, 3]])
print(A+B)                      # [[ 4  2  4]
                                #  [ 4 11  9]]
print(A*B)                      # [[ 3  0  3]
                                # [ 0 30 18]]

A = np.array([[1,2, 3], [4, 5, 6]])
B = np.array([10,20,30])
print(A*B)                      # [[ 10  40  90]
                                #  [ 40 100 180]]

A = np.array([[1,2], [3,4]])
B = np.array([[3, 0], [0, 6]])
# print(A/B)        # 에러
print(A * 10)                   # [[10 20]
                                # [30 40]]
B = np.array([[3, 2], [2, 6]])
print(A/B)                      # [[0.33333333 1.        ]
                                # [1.5        0.66666667]]



print('###### 4 #####')
# 4. 원소접근
X = np.array([[51,55], [14,19], [0,4]])
print(X)                        #[[51 55]
                                # [14 19]
                                # [ 0  4]]
print(X[0])                     # [51 55]
print(X[0][1])                  # 55
print(X[2][0])                  # 0

for row in X:                   # for로 각 원소에 접금
    print(row)                  # [51 55]
                                # [14 19]
                                # [0 4]

X = X.flatten()
print(X)                        # [51 55 14 19  0  4] : 1차원 배열로 변환
print(X[np.array([0, 2, 4])])     # [51 14  0]  : 인덱스가 0, 2, 4 인 원소 얻기
print((X > 15).dtype)             # bool
print(X > 15)                   # [ True  True False  True False False]
print(X[X > 15])                  # [51 55 19]








########################################
print('###################################')
# 배열 or 행렬 계산 - NumPy(Numerical Python : 과학적 계산(선형대수))
# 1. 배열 생성
x = np.array([10, 20, 30])
print(x)                # [10 20 30]
print(type(x))          # <class 'numpy.ndarray'>
print(x.shape)          # (3,)
print(x[0], x[1], x[2]) # 10 20 30
x[2] = 50
print(x)                # [10 20 50]

y = np.array([[1, 2, 3],[4, 5, 6]])
print(y)
print(y.shape) # (2, 3)

print(y[0][1]) # 2
print(y[0,1])  # 2

print(y[1][0]) # 4
print(y[1,0]) # 4

# z = np.array([1, 2, 3],[4, 5, 6]) # TypeError: data type not understood


# 2. 산술 연산
x = np.array([1., 2., 3.]) # np.array([1., 2., 3., 4.]) - error
y = np.array([4., 5., 6.])
print(x + y)    # [5. 7. 9.]
print(x - y)    # [-3. -3. -3.]
print(x * y)    # [ 4. 10. 18.]
print(x / y)    # [0.25 0.4  0.5 ]

x = np.array([1., 2., 3.])
print(x / 2.0) # [0.5 1.  1.5]


# 3. N차원 배열
A = np.array([[1, 2],[3, 4]])
print(A)
print(A.shape) # (2, 2)
print(A.dtype) # int32

B = np.array([[3,1],[1,6]])

print(A + B)
#[[ 4  2]
# [ 3 10]]

print(A - B)
#[[-2  2]
# [ 3 -2]]

print(A * B)
#[[ 3  0]
# [ 0 24]]

print(A / B)
#[[0.33333333        inf]
# [       inf 0.66666667]]

print(A * 10)
#[[10 20]
# [30 40]]

# 4. 브로드캐스트
X = np.array([[1, 2], [3, 4]])
Y = np.array([10,20])

print(X + Y)
print(X - Y)
print(X * Y)
print(X / Y)

"""
# cf) 주의
Y = np.array([10,20,30])
print(X + Y) # error
print(X - Y)
print(X * Y)
print(X / Y)
"""

# 5. 원소 접근(index)
X = np.array([[51,55], [14,19], [0,4]])
print(X.shape)  # (3, 2)
print(X)        #[[51 55]
                # [14 19]
                # [ 0  4]]
print(X[0])     # [51 55]
print(X[0][1])  # 55

X = X.flatten()
print(X)  # [51 55 14 19  0  4]
print(X[np.array([0,2,4])])   # [51 14  0]

print(X > 15)
print(X[X > 15])
