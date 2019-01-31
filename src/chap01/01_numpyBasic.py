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
print(X[np.array([0,2,4])])     # [51 14  0]  : 인덱스가 0, 2, 4 인 원소 얻기
print((X>15).dtype)             # bool
print(X > 15)                   # [ True  True False  True False False]
print(X[X>15])                  # [51 55 19]








