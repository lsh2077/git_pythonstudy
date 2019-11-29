import numpy as np


def seq_array():
    data1 = list(range(0,10));
    print(type(data1), data1)
    a1 = np.array(data1)
    print(type(a1), a1.dtype, a1)

    data2 = [0.1, 5, 4, 12, 0.5]
    a2 = np.array(data2)
    print(type(a2), a2.dtype, a2)


def two_dimension_array():
    a3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # 2차원 배열
    print(a3.dtype, a3, a3.shape)


def range_array():
    print("====range_array====")
    print("np.arange(0, 10, 2) :", np.arange(0, 10, 2))
    print("np.arange(1, 10) :", np.arange(1, 10))
    print("np.arange(5) :", np.arange(5))

    # 2차원 배열
    b1 = np.arange(12).reshape(4, 3) # 4행 3열
    print("b1.shape", b1.shape)
    print("np.arange(12).reshape(4,3) :", b1)

    print("np.arange(5) : {}\nnp.arange(5).shape : {}".format(np.arange(5), np.arange(5).shape))


def num_array():
    print("====num_array====")
    n1 = np.linspace(1, 10, 10)
    print("np.linspace(1, 10, 10) : {} dtype : {} len {}".format(n1, n1.dtype, len(n1)))
    n2 = np.linspace(0, np.pi, 20)
    print("np.linspace(0, np.pi, 20) : {} dtype : {} len {}".format(n2, n2.dtype, len(n2)))
    print(np.zeros(10))
    # 2차원 배열 생성
    print(np.zeros((3,4)))
    print(np.ones(5))
    # 2차원 배열 생성
    print(np.ones((3,5)))
    # 3X3 단위행렬
    print(np.eye(3))


def type_conversion():
    str_array = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
    print("np.array : {} dtype : {}".format(str_array, str_array.dtype))
    float_array = str_array.astype(float)
    print("float_array : {} dtype : {}".format(float_array, float_array.dtype))


def rand_array():
    print(np.random.rand(2,3))
    print(np.random.rand())
    print(np.random.rand(2,3,4))
    # 지정범위에 해당하는 정수로 난수 배열을 생성
    print(np.random.randint(10, size=(3, 4)))
    print(np.random.randint(1,30))
    np.random.seed(1)
    rand01 = np.random.rand(2,3)
    print("rand01.dtype : {} rand01 : {}".format(rand01.dtype, rand01))


def array_expression():
    arr1 = np.array([10, 20, 30, 40])
    arr2 = np.array([1, 2, 3, 4])
    print(arr1 + arr2)
    print(arr1 - arr2)
    print(arr2*2)
    print(arr2**2)
    print(arr1*arr2)
    print(arr1/arr2)
    print(arr1/(arr2**2))
    print(arr1>20)

    arr3 = np.arange(5)
    print("배열 arr3 : {}".format(arr3))
    # 배열의 합과 평균
    print("합 :{}, 평균 :{}".format(arr3.sum(), arr3.mean()))
    # 배열의 표준편차와 분산
    print("표준편차 :{}, 분산 :{}".format(arr3.std(), arr3.var()))
    print("최솟값 :{}, 최댓값 :{}".format(arr3.min(), arr3.max()))

    arr4 = np.arange(1,5)
    print("배열 arr4 : {}".format(arr4))
    print("누적합 : {}, 누적곱 : {}".format(arr4.cumsum(), arr4.cumprod()))


def array_matrix():
    A = np.array([0, 1, 2, 3]).reshape(2,2)
    print("==A행렬==")
    print(A)

    B = np.array([3, 2, 0, 1]).reshape(2,2)
    print("==B행렬==")
    print(B)

    print("==행렬곱==")
    print(A.dot(B))

    print("==행렬곱2==")
    print(np.dot(A,B))

    print("==전치행렬==")
    print(np.transpose(A))

    print("==전치행렬2==")
    print(A.transpose())

    print("==역행렬==")
    print(np.linalg.inv(A))

    print("==행렬식==")
    print(np.linalg.det(A))


def indexing_ex():
    print("======인덱싱======")
    a1 = np.array([0, 10, 20, 30, 40, 50])
    print(a1)
    print(a1[0])
    print(a1[4])
    # 원소 변경 가능
    a1[5] = 70
    print(a1)
    print(a1[[1,3,4]])

    a2 = np.arange(10, 100, 10).reshape(3,3)
    print(a2)
    print(a2[0, 2])
    a2[2, 2] = 95
    print(a2)
    print(a2[1])
    a2[1] = np.array([45, 55, 65])
    print(a2)
    a2[1] = [47, 57, 67]
    print(a2)
    print(a2[[0,2], [0,1]])

    a = np.array([1, 2, 3, 4, 5, 6])
    print(a[a>3])
    print(a[(a%2)==0])


def slicing_ex():
    print("======슬라이싱======")
    b1 = np.array([0, 10, 20, 30, 40, 50])
    # 시작위치 : 끝위치-1
    print(b1[1:4])
    print(b1[:3])
    print(b1[2:])
    b1[2:5] = np.array([25, 35, 45])
    print(b1)
    b1[3:6] = np.array([60])
    print(b1)

    b2 = np.arange(10, 100, 10).reshape(3, 3)
    print(b2)
    # 행시작위치:행끝위치, 열시작위치:열끝위치
    print(b2[1:3, 1:3])
    print(b2[:3, 1:])
    # 행을 지정하고 열을 슬라이싱
    print(b2[1][0:2])
    print(b2[0:2, 1:3])
    b2[0:2, 1:3] = np.array([[25, 35], [55, 65]])
    print(b2)


if __name__ == "__main__":
    seq_array()
    two_dimension_array()
    range_array()
    num_array()
    type_conversion()
    rand_array()
    array_expression()
    array_matrix()
    indexing_ex()
    slicing_ex()