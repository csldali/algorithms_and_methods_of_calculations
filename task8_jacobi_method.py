import math
import numpy
import pprint


def create_the_matrix():
    n = 4
    array = numpy.full((n, n), 1)
    i_task = 13 + 2

    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                array[i][j] = (i_task % 10) + (i_task * 0.1)

    array[1][0] = array[0][0] / 2
    array[2][1] = array[0][0] / 2
    array[3][2] = array[0][0] / 2

    array[0][1] = array[0][0] / 2
    array[1][2] = array[0][0] / 2
    array[2][3] = array[0][0] / 2

    array[0][2] = array[0][0] / 4
    array[1][3] = array[0][0] / 4

    array[2][0] = array[0][0] / 4
    array[3][1] = array[0][0] / 4

    array[0][3] = -array[0][0] / 4
    array[3][0] = -array[0][0] / 4

    return array


def jacobi(A, e):  # Jacobi method

    def maxElem(A):  # Find largest off-diag. element a[k,l]
        n = len(A)
        max_a = 0
        p = 0
        q = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(A[i, j]) >= max_a:
                    max_a = abs(A[i, j])
                    p = i
                    q = j
        return max_a, p, q

    def rotate(A, p, q):  # Rotate to make a[k,l] = 0
        aDiff = A[q, q] - A[p, p]
        if abs(A[p, q]) < abs(aDiff) * e:
            t = aDiff / (2 * A[p, q])
            #return t
        else:
            tao = aDiff / (2.0 * A[p, q])
            t = 1.0 / (abs(tao) + math.sqrt(tao ** 2 + 1.0))
            if tao < 0.0:
                t = -t
        c = 1.0 / math.sqrt(1 + t ** 2)
        s = t * c
        temp = A[p, q]
        A[p, q] = 0.0
        A[p, p] = A[p, p] - t * temp
        A[q, q] = A[q, q] + t * temp

    res_A = numpy.diagonal(A)
    res_A = res_A[::-1]
    while True:  # Jacobi rotation loop
        max_a, p, q = maxElem(A)
        if max_a < e: return res_A
        rotate(A, p, q)


if __name__ == '__main__':
    array = create_the_matrix()
    e = 1e-10

    print("||| The Matrix:")
    pprint.pprint(array)

    print("\n||| Custom Jacobi method:")
    pprint.pprint(jacobi(array, e))

    print("\n||| numpy.linalg.eig():")
    w, _ = numpy.linalg.eig(array)
    pprint.pprint(w)
    print("\n\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    array1 = numpy.array([[1., -1., 0.],
                          [-1., 2., 1.],
                          [0., 1., 5.]])
    print("||| The Matrix:")
    pprint.pprint(array1)

    print("\n||| Custom Jacobi method:")
    pprint.pprint(jacobi(array1, e))

    print("\n||| numpy.linalg.eig():")
    w, _ = numpy.linalg.eig(array1)
    pprint.pprint(w)
    print("\n\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    array2 = numpy.array([[10., -1., 2., 0.],
                          [-1., 11., -1., 3.],
                          [2., -1., 10., -1.],
                          [0.0, 3., -1., 8.]])
    print("||| The Matrix:")
    pprint.pprint(array2)

    print("\n||| Custom Jacobi method:")
    pprint.pprint(jacobi(array2, e))

    print("\n||| numpy.linalg.eig():")
    w, _ = numpy.linalg.eig(array2)
    pprint.pprint(w)
    print("\n\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    array3 = numpy.matrix([[6.29, 0.97, 1.00, 1.10],
                           [0.97, 4.13, 1.30, 0.16],
                           [1.00, 1.30, 5.47, 2.10],
                           [1.1, 0.16, 2.10, 6.07]])
    print("||| The Matrix:")
    pprint.pprint(array3)

    print("\n||| Custom Jacobi method:")
    pprint.pprint(jacobi(array3, e))

    print("\n||| numpy.linalg.eig():")
    w, _ = numpy.linalg.eig(array3)
    pprint.pprint(w)
