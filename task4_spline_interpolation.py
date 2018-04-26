import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x * math.sin(x)


## Tri Diagonal Matrix Algorithm(a.k.a Thomas algorithm) solver
def TDMA(a, b, c, d):
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


initial_plot = {}
x = np.array()
y = np.array()
for i in np.arange(-math.pi, math.pi, 1):
    initial_plot[i] = f(i)



print(np.linalg.solve(x, y))

# Plot construction
fig = plt.gcf()
fig.canvas.set_window_title('Plot construction')
plt.grid(True)
plt.title(u'Plots')
plt.xlabel(u'Argument [x]')
plt.ylabel(u'Function [f(x)]')

plt.plot(initial_plot.keys(), initial_plot.values(), label=u'initial_plot', color='k')

plt.scatter(x, x, label=u"x", color='r')

plt.legend()
plt.show()
