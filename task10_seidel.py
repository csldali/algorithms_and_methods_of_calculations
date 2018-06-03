import pprint
import scipy
import numpy


def seidel(A, e):
    n = len(A)
    x0 = [0] * n
    x1 = x0[:]
    while True:
        for i in range(n):
            s = sum(-A[i][j] * x1[j] for j in range(n) if i != j)
            x1[i] = (A[i][n] + s) / A[i][i]
        if all(abs(x1[i] - x0[i]) < e for i in range(n)):
            for i in range(n):
                if x1[i] >= 0:
                    x1[i] = round(abs(x1[i]))
                else:
                    x1[i] = -round(abs(x1[i]))
            return x1
        x0 = x1[:]


if __name__ == '__main__':
    system = scipy.array([
        [1., 2., 3., 3.],
        [3., 5., 7., 0.],
        [1., 3., 4., 1.],
    ])
    e = 0.005
    print("||| Initial system:")
    pprint.pprint(system)
    print("\n||| the roots by custom Seidel method:")
    print(seidel(system, e))
    print("\n||| numpy.linalg.solve:")
    m = [1., 2., 3.], [3., 5., 7.], [1., 3., 4.]
    b = [3, 0, 1]
    print(numpy.linalg.solve(m, b))
