import pprint
import numpy
import scipy.linalg


def triangular_matrix(array):
    n = len(array)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            koef = array[j][i] / array[i][i]
            for k in range(i, n + 1):
                array[j][k] -= array[i][k] * koef
    return array


def detSolve(array):
    n = len(array)
    det = numpy.zeros(n)
    for i in range(n - 1, -1, -1):
        buf = 0
        for j in range(i, n):
            buf = buf + array[i][j] * det[j]
            det[i] = (array[i][n] - buf) / array[i][i]
    return det


def lu_decomposition(A):
    n = len(A)
    """
    for i in range(1, n + 1):
        for j in range(i, n - 1):
            buf_sum = 0
            for k in range(0, i - 1):
                buf_sum += L[i][k] * U[k][j]
            U[i][j] = A[i][j] - buf_sum

    for i in range(1, n + 1):
        for j in range(i, n - 1):
            buf_sum = 0
            for k in range(0, i - 1):
                buf_sum += L[j][k] * U[k][i]
            L[j][i] = (A[j][i] - buf_sum) / U[i][i]

    """

    """
    for j in range(0, n):
        U[0][j] = A[0][j]
        if U[0][0] != 0:
            L[j][0] = A[j][0] / U[0][0]
    """

    for i in range(1, n):
        buf_sum = 0.
        for j in range(i, n - 1):
            if i >= j:
                # Upper
                for k in range(0, i - 1):
                    buf_sum += L[i][k] * U[k][j]
                U[i][j] = A[i][j] - buf_sum
            if i > j:
                # Lower
                for k in range(0, i - 1):
                    buf_sum += L[j][k] * U[k][i]
                L[j][i] = (A[j][i] - buf_sum) / U[i][i]
    return L, U


if __name__ == '__main__':

    system = scipy.array([
        [1., 2., 3., 3.],
        [3., 5., 7., 0.],
        [1., 3., 4., 1.],
    ])

    P, L, U = scipy.linalg.lu(system)
    print("\n|||||||||||||||||||||||| scipy.linalg.lu |||||||||||||||||||||||\nL:")
    pprint.pprint(L)
    print("U:")
    pprint.pprint(U)
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    L, U = lu_decomposition(system)
    print("\n||||||||||||||||| custom lu_decomposition |||||||||||||||||||||||||\n=== custom L:")
    pprint.pprint(L)
    print("\n=== custom U:")
    pprint.pprint(U)
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("\n-------------------- The Gauss Method -----------------------")
    n = len(system)
    print("\noriginal matrix:")
    pprint.pprint(system)
    print("\ntriangular matrix:")
    system = triangular_matrix(system)
    pprint.pprint(system)
    print("\nthe roots:")
    det = detSolve(system)
    for x in det: print(x)
    print("-------------------- end Gauss Method -----------------------")
