import pprint

from numpy import array, identity, diagonal
from math import sqrt
import numpy

"""

def jacobi(a, tol=1.0e-10):  # Jacobi method

    def maxElem(a):  # Find largest off-diag. element a[k,l]
        n = len(a)
        aMax = 0.0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(a[i, j]) >= aMax:
                    aMax = abs(a[i, j])
                    k = i
                    l = j
        return aMax, k, l

    def rotate(a, p, k, l):  # Rotate to make a[k,l] = 0
        n = len(a)
        aDiff = a[l, l] - a[k, k]
        if abs(a[k, l]) < abs(aDiff) * tol:
            t = a[k, l] / aDiff
        else:
            phi = aDiff / (2.0 * a[k, l])
            t = 1.0 / (abs(phi) + sqrt(phi ** 2 + 1.0))
            if phi < 0.0: t = -t
        c = 1.0 / sqrt(t ** 2 + 1.0)
        s = t * c
        tau = s / (1.0 + c)
        temp = a[k, l]
        a[k, l] = 0.0
        a[k, k] = a[k, k] - t * temp
        a[l, l] = a[l, l] + t * temp
        for i in range(k):  # Case of i < k
            temp = a[i, k]
            a[i, k] = temp - s * (a[i, l] + tau * temp)
            a[i, l] = a[i, l] + s * (temp - tau * a[i, l])
        for i in range(k + 1, l):  # Case of k < i < l
            temp = a[k, i]
            a[k, i] = temp - s * (a[i, l] + tau * a[k, i])
            a[i, l] = a[i, l] + s * (temp - tau * a[i, l])
        for i in range(l + 1, n):  # Case of i > l
            temp = a[k, i]
            a[k, i] = temp - s * (a[l, i] + tau * temp)
            a[l, i] = a[l, i] + s * (temp - tau * a[l, i])
        for i in range(n):  # Update transformation matrix
            temp = p[i, k]
            p[i, k] = temp - s * (p[i, l] + tau * p[i, k])
            p[i, l] = p[i, l] + s * (temp - tau * p[i, l])

    n = len(a)
    res_a = diagonal(a)
    if n % 2 == 0:
        res_a = res_a[::-1]

    maxRot = 5 * (n ** 2)  # Set limit on number of rotations
    p = identity(n) * 1.0  # Initialize transformation matrix
    while True:  # Jacobi rotation loop
        aMax, k, l = maxElem(a)
        if aMax < tol: return res_a
        rotate(a, p, k, l)
    else:
        print('Jacobi method did not converge')


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


array = create_the_matrix()
pprint.pprint(jacobi(array))

w, _ = numpy.linalg.eig(array)
pprint.pprint(w)

       for i in range(p):  # Case of i < p
           temp = A[i, p]
           A[i, p] = temp - s * (A[i, q] + tau * temp)
           A[i, q] = A[i, q] + s * (temp - tau * A[i, q])

       for i in range(p + 1, q):  # Case of p < i < q
           temp = A[p, i]
           A[p, i] = temp - s * (A[i, q] + tau * A[p, i])
           A[i, q] = A[i, q] + s * (temp - tau * A[i, q])

       for i in range(q + 1, n):  # Case of i > q
           temp = A[p, i]
           A[p, i] = temp - s * (A[q, i] + tau * temp)
           A[q, i] = A[q, i] + s * (temp - tau * A[q, i])

       for i in range(n):  # Update transformation matrix
           temp = B[i, p]
           B[i, p] = temp - s * (B[i, q] + tau * B[i, p])
           B[i, q] = B[i, q] + s * (temp - tau * B[i, q])

"""

import scipy


def gauss_seidel(A, e):
    n = len(A)
    x0 = [0] * n
    x1 = x0[:]
    while True:
        for i in range(n):
            s = sum(-A[i][j] * x1[j] for j in range(n) if i != j)
            x1[i] = round((A[i][n] + s) / A[i][i], 3)
        if all(abs(x1[i] - x0[i]) < e for i in range(n)):
            return x1
        x0 = x1[:]


if __name__ == '__main__':
    system = scipy.array([
        [1., 2., 3., 3.],
        [3., 5., 7., 0.],
        [1., 3., 4., 1.],
    ])
    e = 1e-5
    print(gauss_seidel(system, e))

    m = [1., 2., 3.], [3., 5., 7.], [1., 3., 4.]
    b = [3, 0, 1]
    print(numpy.linalg.solve(m, b))
