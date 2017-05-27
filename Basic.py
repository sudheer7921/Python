#수업정리
#수업 자료: https://www.slideshare.net/dahlmoon/numpy-20160519

# coding=utf-8
import numpy as np
import time

#ndarray와 Matrix의 구분
'''
a1 = np.array([1, 2, 3])
# 크기(3,)인 1차원 배열

a2 = np.array([ [1, 2, 3 ] ])
# 크기(1,3)인 2차원 배열(행벡터)

a3 = np.array([ [1], [2], [3] ])
# 크기(3,1)인 2차원 배열(열벡터)

print (a1)
print (a1.ndim, a1.shape) #
print (a2)
print (a2.ndim, a2.shape) #
print (a3)
print (a3.ndim, a3.shape) #
'''
'''
m1 = np.matrix([1, 2, 3, 4]) #Matlab 연산 지원한다.

print(m1*m1.T) #행렬의 * 연산자는 행렬 곱 -> [[30]]
print(m1.dot(m1.T)) #행렬의 dot은 행렬 곱 -> [[30]]
print(np.multiply(m1,m1)) #행렬의 multiply는 요소간 곱 -> [[1 4 9 16]]

a1 = np.array([1, 2 ,3, 4]) #ndarray

print(a1.T) #배열은 행렬로 생각 안해서 Transpose 할수 없나 보다 -> [1 2 3 4]
print(a1*a1.T) #배열의 * 연산자는 요소간 곱 -> [1 4 9 16]
print(a1.dot(a1.T)) #배열의 dot은 행렬곱 -> 30
print(np.multiply(a1,a1)) #배열의 multiply는 요소간 곱 -> [1 4 9 16]
'''

#ndarray class
#Ndarray는 데이터를 관리, data-type은 실제 데이터들의 값을 관리, array scalar는 위치를 관리

#ndarray는 각 원소별로 동일한 데이터 타입으로 처리
'''
l = [1, 2, 3, 4]
a = np.array(l,np.int)
print(a) # [1 2 3 4]
a = np.array(l,np.float)
print(a) # [1. 2. 3. 4.]
a = np.array(l,np.str)
print(a) # ['1' '2' '3' '4']
'''
'''
#0차원 배열
#numpy.array 생성시 단일값(Scalar Value)를 넣으면 array 타입이 아닌, 일반 타입을 만듬
a = np.array(10)
print(a)
print(a.ndim)

#1차원 배열
a = np.array([1, 2, 3, 4])
print(a) # [1 2 3 4]
print(a.ndim) # 1

#2차원 배열
a = np.array([[1,2],[3,4]])
print(a)
print(a.ndim)

#3차원 배열
a = np.array([ [[1,2],[3,4]], [[5,6],[7,8]] ])
print(a)
print(a.ndim)

#할당은 참조만 전달
a = np.array([1, 2, 3, 4])
s = a[:2] # 처음부터 2번째 원소까지만 슬라이스
ss = a[:2].copy # 복사
print(s.size) # 2
s[0] = 99
print(a) # [99 2 3 4]
print(s) # [99 2]
print(ss) # [1 2]

#벡터화 연산: for문 미사용
cvalues = [25.3, 24.8, 26.9, 23.9] #섭씨 ndarray 생성
C = np.array(cvalues)
print(C)
F = C * 9 / 5 + 32
#print type(F), F

#기존 방식, numpy 라이브러리를 안썼을 때, 리스트 Comprehension도 Loop문 실행(?)
F1 = [ x * 9/5 + 32 for x in cvalues]
#print type(F1), F1

#브로드 캐스팅
A = np.array([ [11, 12, 13], [21, 22, 23], [31, 32, 33] ])
B = np.array([1, 2, 3])
print(A * B) # 차원이 맞지 않기에 배열 B가 3차원 행렬로 확장한다.
print(A + B)

#ndarray와 python list 타입의 연산 속도 비교
size_of_vec = 10000

def pure_python_version():
    t1 = time.time()
    X = range(size_of_vec)
    Y = range(size_of_vec)
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])
    print(t1)
    return time.time() - t1

def numpy_version():
    t2 = time.time()
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    Z = X + Y
    print(t2)
    return time.time() - t2 #

t1 = pure_python_version()
t2 = numpy_version()
print(t1, t2) #t2 크기가 너무 작아 0으로  프린트 된다.
#print ( "numpy_version is faster " + str(t1/t2) + "than pure_python_version")
'''










