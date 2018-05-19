import pprint
import numpy
import scipy.linalg


def triangular_matrix(system):
    n = len(system)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            koef = system[j][i] / system[i][i]
            for k in range(i, n + 1):
                system[j][k] -= system[i][k] * koef
    return system


if __name__ == '__main__':

    system = [
        [1., 2., 3., 3.],
        [3., 5., 7., 0.],
        [1., 3., 4., 1.],
    ]
    n = len(system)

    print("\noriginal array:")
    for i in system: print(i)

    print("\ntriangular_matrix array:")
    system = triangular_matrix(system)
    for j in system: print(j)

    print("\ndet array:")
    det = numpy.zeros(n)

    for i in range(n - 1, -1, -1):
        buf = 0
        for j in range(i, n):
            buf = buf + system[i][j] * det[j]
            det[i] = (system[i][n] - buf) / system[i][i]
    for x in det: print(x)

    P, L, U = scipy.linalg.lu(system)
    print("\n\n\nA:")
    pprint.pprint(system)
    print("P:")
    pprint.pprint(P)
    print("L:")
    pprint.pprint(L)
    print("U:")
    pprint.pprint(U)


