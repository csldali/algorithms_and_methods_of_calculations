import numpy
import matplotlib.pyplot as plt
import math
import scipy.integrate

# The function given by task
def f(x, y):
    return x * y + math.e ** (0.1 * x)

# The Heun method
def heun_method_solver(f, x, h, start_points):
    y = numpy.zeros((n + 1,))
    x[0], y[0] = start_points
    for i in range(1, n + 1):
        f1 = f(x[i - 1], y[i - 1])
        f2 = f(x[i - 1] + (2.0 / 3.0) * h, y[i - 1] + (2.0 / 3.0) * h * f1)
        y[i] = y[i - 1] + h * (f1 + 3.0 * f2) / 4.0
    return y

x0 = 0
y0 = 1
n = 10
h = (y0 - x0) / n
start_points = (x0, y0)
X = numpy.arange(x0, y0 + h, h)
Y = scipy.integrate.odeint(f, y0, X)
heun_method_Y = heun_method_solver(f, X, h, start_points)

fig = plt.gcf()
fig.canvas.set_window_title('Plot construction')
plt.grid(True)
plt.title(u'Plots')
plt.xlabel(u'Argument [x]')
plt.ylabel(u'Function [f(x)]')
plt.plot(X, Y, label='Initial plot (scipy.integrate.odeint)', color='k')
plt.plot(X, heun_method_Y, label='Heun plot (heun_method_solver)', color='r')
plt.legend()
plt.show()
