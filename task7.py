import pprint
import math
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


def find_max_by_abs(lst):
    elements = set(lst)
    for elem in elements:
        lesser_elements_count = 0
        for curr_elem in elements:
            if abs(elem) > abs(curr_elem):
                lesser_elements_count += 1
        if lesser_elements_count == len(elements) - 1:
            return elem


def find_min_by_abs(lst):
    elements = set(lst)
    for elem in elements:
        lesser_elements_count = 0
        for curr_elem in elements:
            if abs(elem) < abs(curr_elem):
                lesser_elements_count += 1
        if lesser_elements_count == len(elements) - 1:
            return elem


def inverse_iteration_min(A):
    A_1 = numpy.linalg.inv(A)
    y0 = numpy.ones(len(A))
    y0_norm = math.sqrt(sum(y0))
    x0 = numpy.zeros(len(y0))
    for i in range(len(y0)):
        x0[i] = y0[i] / y0_norm
    x_next = x0
    lam0 = 3
    while True:
        y_next = numpy.dot(A_1, x_next)
        lam1 = numpy.dot(y_next, x_next)
        y_next_norm = math.sqrt(sum(y_next))
        x_next = numpy.zeros(len(x_next))
        for i in range(len(x_next)):
            x_next[i] = y_next[i] / y_next_norm
        if abs(lam1 - lam0) < 0.005 * abs(lam1):
            return round(1 / lam1)
        else:
            lam0 = lam1


def inverse_iteration_max(A):
    sigma = 3
    A_sigma = A - sigma * numpy.eye(len(A))  # bug
    A_1 = numpy.linalg.inv(A_sigma)
    y0 = numpy.ones(len(A_sigma))
    y0_norm = math.sqrt(sum(y0))
    x0 = numpy.zeros(len(y0))
    for i in range(len(y0)):
        x0[i] = y0[i] / y0_norm
    x_next = x0
    lam0 = 3
    while True:
        y_next = numpy.dot(A_1, x_next)
        lam1 = numpy.dot(y_next, x_next)
        y_next_norm = math.sqrt(sum(y_next))
        x_next = numpy.zeros(len(x_next))
        for i in range(len(x_next)):
            x_next[i] = y_next[i] / y_next_norm
        if abs(lam1 - lam0) < 0.005 * abs(lam1):
            return round(1 / lam1) - sigma  # !!!
        else:
            lam0 = lam1


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


if __name__ == '__main__':
    array = create_the_matrix()
    pprint.pprint(array)
    e = 10e-6

    print("\n1)\nMax value with internal method:")
    a, b = numpy.linalg.eig(array)
    print("numpy.linalg.eig(array):\t", a.max())
    max_ev = power_iteration(array, e)
    print("custom method - power_iteration(array, e):\t", max_ev)

    print(
        "\n||||||||||||||||||||||||||||||||||||||||||||||\n2)\nMax and min value with Inverse iteration method:\n\nMax:")

    print("numpy.linalg.eig(array):\t", max_ev)
    print("custom method - inverse_iteration_max(array, e):\t", inverse_iteration_max(array))

    print("\nMin:\nnumpy.linalg.eig(array):\t", find_min_by_abs(a))
    print("custom method - inverse_iteration_min(array, e):\t", inverse_iteration_min(array))
