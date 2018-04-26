import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


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
    print(type(c))
    print(A)
    print(Ff)
    print(np.linalg.solve(A, Ff))
    d = np.zeros((n,))
    b = np.zeros((n,))
    S = n * [0]
    for i in range(n):
        d[i] = (c[i + 1] - c[i]) / h
        b[i] = (F[i + 1] - F[i]) / h - h / 2 * c[i] - h * h / 6 * d[i]
        S[i] = a[i] + b[i] * (x - X[i]) + c[i] / 2 * (x - X[i]) ** 2 + d[i] / 6 * (x - X[i]) ** 3
    return S


def f(x):
    return x * np.sin(x)


def TDMAsolver(a, b, c, d):
    '''
    TDMA solver, a b c d can be NumPy array type or Python list type.
    refer to http://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
    and to http://www.cfd-online.com/Wiki/Tridiagonal_matrix_algorithm_-_TDMA_(Thomas_algorithm)
    '''
    nf = len(d)  # number of equations
    ac, bc, cc, dc = map(np.array, (a, b, c, d))  # copy arrays
    for it in range(1, nf):
        mc = ac[it - 1] / bc[it - 1]
        bc[it] = bc[it] - mc * cc[it - 1]
        dc[it] = dc[it] - mc * dc[it - 1]

    xc = bc
    xc[-1] = dc[-1] / bc[-1]

    for il in range(nf - 2, -1, -1):
        xc[il] = (dc[il] - cc[il] * xc[il + 1]) / bc[il]

    return xc


a = np.array([4., 1., 0.])
b = np.array([1., 4., 1.])
c = np.array([0., 1., 4.])
d = np.array([-2.72837045, 3.27404454, -2.72837045])

print("Test results:")

print(TDMAsolver(a, b, c, d))

print("end Test results:")

a = -np.pi
b = np.pi
x = sym.Symbol('x')
n = 5
h = (b - a) / n
X = np.linspace(a, b, num=n)
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
plt.plot(XX, f(XX), color='blue')
plt.plot(XX, S3, color='green', ls='--')
plt.scatter(X, F, marker='o', label=u'spline interpolation', color='red')

plt.legend()
# plt.show()
