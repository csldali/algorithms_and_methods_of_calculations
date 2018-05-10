from pylab import *
import numpy
import math
from scipy.linalg import lstsq


def f(x, n, i):
    return g(x, (n % 4), (n % 5)) + ((-1) ** i) * 0.002 * (4 - i)


def g(x, A, B):
    return A * x * (math.e ** (-B * x))


h = (1 / 8)
n = 13

x_array = numpy.zeros((9,))
y_array = numpy.zeros((9,))

f_initial_plot = {}
x = 1
for i in range(0, 9):
    x_array[i] = x
    y_array[i] = f(x, n, i)
    f_initial_plot[x] = f(x, n, i)
    x = x + h

M = x_array[:, np.newaxis] ** [0, 1]
p, res, rnk, s = lstsq(M, y_array)


g_plot = {}
x = 1
for i in range(0, 9):
    g_plot[x] = g(x, (n % 4), (n % 5))
    x = x + h

fig = plt.gcf()
fig.canvas.set_window_title('Plot construction')
plt.grid(True)
plt.title(u'Plots')
plt.xlabel(u'Argument [x]')
plt.ylabel(u'Function [f(x)]')
#plt.plot(f_initial_plot.keys(), f_initial_plot.values(), color='b')
plt.scatter(f_initial_plot.keys(), f_initial_plot.values(),
            label=u'f(x)', color='r')
#plt.plot(g_plot.keys(), g_plot.values(), label=u'approximating function\ng(x): A * x * (math.e ** (-B * x))', color='k')

yy = p[0] + p[1] * x_array

plt.plot(x_array, yy, label=u'scipy.linalg.lstsq', color='k')
#plt.scatter(x_array, yy, label=u'', color='g')

plt.legend(shadow=True)
plt.show()
