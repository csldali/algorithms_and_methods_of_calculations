import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import math


def Spline3GI(X, F, a0, b0):
    x = sym.Symbol('x')
    n = len(X) - 1
    a = F[0:n]
    h = (b0 - a0) / n
    A = np.diag(4 * np.ones((n - 1,))) + np.diag(np.ones((n - 2,)), k=1) + np.diag(np.ones((n - 2,)), k=-1)
    Ff = np.zeros((n - 1,))
    for i in range(n - 1):
        Ff[i] = (6 * (F[i] - 2 * F[i + 1] + F[i + 2])) / h / h
    c = np.zeros((n + 1,))
    c[1:n] = np.linalg.solve(A, Ff)  # решить СЛАУ методом прогонки!
    # print(type(c))
    # print(A)
    # print("F(x)" + str(Ff))
    # print("Correct result\n" + str(np.linalg.solve(A, Ff)))
    d = np.zeros((n,))
    b = np.zeros((n,))
    S = n * [0]
    for i in range(n):
        d[i] = (c[i + 1] - c[i]) / h
        b[i] = (F[i + 1] - F[i]) / h - h / 2 * c[i] - h * h / 6 * d[i]
        S[i] = a[i] + b[i] * (x - X[i]) + c[i] / 2 * (x - X[i]) ** 2 + d[i] / 6 * (x - X[i]) ** 3
    return S


def cubic_interpolation(x0, x, y):
    x = np.asfarray(x)
    y = np.asfarray(y)
    # check if sorted
    if np.any(np.diff(x) < 0):
        indexes = np.argsort(x)
        x = x[indexes]
        y = y[indexes]

    size = len(x)

    xdiff = np.diff(x)
    ydiff = np.diff(y)

    # allocate buffer matrices
    Li = np.empty(size)
    Li_1 = np.empty(size - 1)
    z = np.empty(size)

    # fill diagonals Li and Li-1 and solve [L][y] = [B]
    Li[0] = math.sqrt(2 * xdiff[0])
    Li_1[0] = 0.0
    B0 = 0.0  # natural boundary
    z[0] = B0 / Li[0]

    for i in range(1, size - 1, 1):
        Li_1[i] = xdiff[i - 1] / Li[i - 1]
        Li[i] = math.sqrt(2 * (xdiff[i - 1] + xdiff[i]) - Li_1[i - 1] * Li_1[i - 1])
        Bi = 6 * (ydiff[i] / xdiff[i] - ydiff[i - 1] / xdiff[i - 1])
        z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    i = size - 1
    Li_1[i - 1] = xdiff[-1] / Li[i - 1]
    Li[i] = math.sqrt(2 * xdiff[-1] - Li_1[i - 1] * Li_1[i - 1])
    Bi = 0.0  # natural boundary
    z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    # solve [L.T][x] = [y]
    i = size - 1
    z[i] = z[i] / Li[i]

    for i in range(size - 2, -1, -1):
        z[i] = (z[i] - Li_1[i - 1] * z[i + 1]) / Li[i]

    # find index
    index = x.searchsorted(x0)
    np.clip(index, 1, size - 1, index)

    xi1, xi0 = x[index], x[index - 1]
    yi1, yi0 = y[index], y[index - 1]
    zi1, zi0 = z[index], z[index - 1]
    hi1 = xi1 - xi0

    # calculate cubic
    f0 = zi0 / (6 * hi1) * (xi1 - x0) ** 3 + \
         zi1 / (6 * hi1) * (x0 - xi0) ** 3 + \
         (yi1 / hi1 - zi1 * hi1 / 6) * (x0 - xi0) + \
         (yi0 / hi1 - zi0 * hi1 / 6) * (xi1 - x0)

    return f0


def f(x):
    return x * np.sin(x)


a = -np.pi
b = np.pi
x = sym.Symbol('x')
n = 5
h = (b - a) / n
X = np.linspace(a, b, num=n + 1)
F = f(X)
S = Spline3GI(X, F, a, b)
XX = np.linspace(a, b)
S3 = np.zeros(XX.shape)
num = 0
for i in range(len(XX)):
    if XX[i] > X[num + 1]:
        num += 1
    S3[i] = S[num].subs(x, XX[i])

fig = plt.gcf()
fig.canvas.set_window_title('Plot construction')
plt.grid(True)
plt.title(u'Plots')
plt.xlabel(u'Argument [x]')
plt.ylabel(u'Function [f(x)]')
plt.plot(XX, f(XX), color='blue', label=u'Initial plot: f(x) = x * sin(x)')
plt.plot(XX, S3, color='green', ls='--')
plt.scatter(X, F, marker='o', label=u'Spline3GI - spline interpolation', color='red')
x_new = np.linspace(a, b, num=n + 1)
# plt.scatter(X, cubic_interpolation(x_new, X, F), marker='o', label=u'cubic_interpolation - spline interpolation',
# color = 'k')
plt.plot(X, cubic_interpolation(x_new, X, F), ls='--', label=u'Tridiagonal matrix algorithm - spline interpolation',
         color='k')
plt.legend()
plt.show()
