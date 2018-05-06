from pylab import *
import numpy
import math


def f_initial(x):
    return x * math.e ** -x


def f(x, n, i):
    return g(x, (n % 4), (n % 5)) + ((-1) ** i) * 0.002 * (4 - i)


def g(x, A, B):
    return A * x * (math.e ** (-B * x))


f_initial_plot = {}

h = (1 / 8)
for x in numpy.arange(1, 2 + h, h):
    f_initial_plot[x] = f_initial(x)

fig = plt.gcf()
fig.canvas.set_window_title('Plot construction')
plt.grid(True)
plt.title(u'Plots')
plt.xlabel(u'Argument [x]')
plt.ylabel(u'Function [f(x)]')

plt.plot(f_initial_plot.keys(), f_initial_plot.values(), label=u'f_initial', color='k')
plt.legend()
plt.show()
