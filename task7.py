import pprint
from copy import deepcopy

import numpy


def create_the_matrix():
    n = 10
    array = numpy.full((n, n), 1)
    i = 13
    alpha = 10 + i / 10
    for i in range(0, n):
        for j in range(0, n):
            if i == 1 and j == 1:
                array[i][j] = alpha
            elif i != j:
                array[i][j] = (i + j) / alpha
    for i in range(1, n - 1):
        array[i + 1][i + 1] = -array[i][i]
    return array


"""
def find_max_by_abs(lst):
    elements = set(lst)
    for elem in elements:
        lesser_elements_count = 0
        for curr_elem in elements:
            if abs(elem) > abs(curr_elem):
                lesser_elements_count += 1
        if lesser_elements_count == len(elements) - 1:
            return elem
"""


def power_iteration(A, e):
    n, d = A.shape
    v = numpy.ones(d) / numpy.sqrt(d)
    ev = eigenvalue(A, v)

    while True:
        Av = A.dot(v)
        v_new = Av / numpy.linalg.norm(Av)
        ev_new = eigenvalue(A, v_new)
        if numpy.abs(ev - ev_new) < e:
            break
        v = v_new
        ev = ev_new
    return ev_new  # , v_new


def eigenvalue(A, v):
    Av = A.dot(v)
    return v.dot(Av)


def inverse_iteration(A, e):

    return 0

if __name__ == '__main__':
    array = create_the_matrix()
    pprint.pprint(array)
    e = 10e-6

    print("\n1)\nMax value with internal method:")
    a, b = numpy.linalg.eig(array)
    print("internal method - numpy.linalg.eig(array):\t", a.max())
    max_ev = power_iteration(array, e)
    print("custom method - power_iteration(array, e):\t", max_ev)

    print("\n2)\nMax and min value with Inverse iteration method:\nMax:")
    print("internal method - numpy.linalg.eig(array):\t", a.max())

    print("custom method - inverse_iteration(array, e):\t", max_ev)
    print("Min:\ninternal method - numpy.linalg.eig(array):\t", a.min())
    #print("custom method - inverse_iteration(array, e):\t", max_ev)
