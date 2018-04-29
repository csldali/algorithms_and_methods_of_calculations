import matplotlib.pyplot as plt
import numpy as np
import math
import sympy


#################################functions area#####################################################################
# The function of the algorithm for finding the Lagrange polynomial
def lagrange(x, y, x_argument, n):
    lagrange_x = 0.0
    p = 1.0
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            if i != j:
                p *= (x_argument - x[j]) / (x[i] - x[j])
        lagrange_x += p * y[i]
        p = 1
    return lagrange_x


# The function given by task
def math_function(x):
    return math.cos(x) / (1 + (math.cos(x) ** 2))


# Counting of step for each point and the function
def get_points(lower_limit, upper_limit, n):
    list_of_points = {}
    h = (upper_limit - lower_limit) / n
    for i in np.arange(0, n + 1, 1):
        list_of_points[lower_limit + i * h] = math_function(lower_limit + i * h)
    return list_of_points


# This function helps to get the valid argument
def correct_index(lower_limit, upper_limit, n, i):
    h = (upper_limit - lower_limit) / n
    return lower_limit + i * h


# The "exclusive" function for main plot
def main_plot(lower_limit, upper_limit, n):
    list_of_points = {}
    h = (upper_limit - lower_limit) / n
    for i in np.arange(0, n + 0.01, 0.01):
        list_of_points[lower_limit + i * h] = math_function(lower_limit + i * h)
    return list_of_points


# The function of the algorithm for finding the Hermite polynomial
from pylab import *


def hermite(n, x):
    if n == 0:
        return ones_like(x) * pi ** (-0.25) * exp(-x ** 2 / 2)

    if n == 1:
        return sqrt(2.) * x * norm * pi ** (-0.25) * exp(-x ** 2 / 2)

    h_i_2 = ones_like(x) * pi ** (-0.25)
    h_i_1 = sqrt(2.) * x * pi ** (-0.25)
    sum_log_scale = zeros_like(x)
    h_i = 0.
    for i in range(2, n + 1):
        h_i = sqrt(2. / i) * x * h_i_1 - sqrt((i - 1.) / i) * h_i_2
        h_i_2, h_i_1 = h_i_1, h_i
        log_scale = log(abs(h_i)).round()
        scale = exp(-log_scale)
        h_i = h_i * scale
        h_i_1 = h_i_1 * scale
        h_i_2 = h_i_2 * scale
        sum_log_scale += log_scale
    return h_i * exp((-x ** 2) / 2 + sum_log_scale)


def f(x):
    return cos(x) / (1 + (cos(x) ** 2))


def f1(x):
    return sin(x) * ((cos(x) ** 2) - 1) * (((cos(x) ** 2) + 1) ** -2)


def f2(x):
    return cos(x) * (((cos(x) ** 2) + 1) ** -3) * (2 * cos(x) ** 2 * sin(x) ** 2 - 6 * sin(x) ** 2 + cos(x) ** 4 - 1)


###########################the end of functions area################################################################


a = -math.pi * 2
b = math.pi * 2
n = 5

func_plot_small_inc = main_plot(a, b, n)
func_plot_int_inc = get_points(a, b, n)
plot_x = []
plot_y = []
hermite_plot = {}

for key, value in func_plot_int_inc.items():
    plot_x.append(key)
    plot_y.append(value)

lagrange_plot = {}

for i in np.arange(0, n + 0.01, 0.01):
    lagrange_plot[correct_index(a, b, n, i)] = lagrange(plot_x, plot_y, correct_index(a, b, n, i), n)

for i in np.arange(0, n + 0.01, 0.01):
    hermite_plot[correct_index(a, b, n, i)] = hermite(n, math_function(correct_index(a, b, n, i)))

# Plot construction
fig = plt.gcf()
fig.canvas.set_window_title('Plot construction')
plt.grid(True)
plt.title(u'Plots')
plt.xlabel(u'Argument [x]')
plt.ylabel(u'Function [f(x)]')

plt.plot(func_plot_small_inc.keys(), func_plot_small_inc.values(), label=u'Main plot with inc. in 0.01', color='k')
plt.plot(func_plot_int_inc.keys(), func_plot_int_inc.values(), label=u'Main plot with inc. in 1', color='m')

plt.plot(lagrange_plot.keys(), lagrange_plot.values(), label=u'The Lagrange plot with inc. in 0.01',
         color='r', ls="--")
lagrange_plot.clear()
for i in np.arange(0, n + 1, 1):
    lagrange_plot[correct_index(a, b, n, i)] = lagrange(plot_x, plot_y, correct_index(a, b, n, i), n)

for i in lagrange_plot:
    plt.scatter(lagrange_plot.keys(), lagrange_plot.values(),
                label=u"x = " + str(round(i, 2)) + " f(x) = " + str(round(lagrange_plot[i], 2)), color='r')

plt.plot(hermite_plot.keys(), hermite_plot.values(), label=u'The Hermite plot', color='b', ls=":")
hermite_plot.clear()
for i in np.arange(0, n + 1, 1):
    hermite_plot[correct_index(a, b, n, i)] = hermite(n, math_function(correct_index(a, b, n, i)))
for i in hermite_plot:
    plt.scatter(hermite_plot.keys(), hermite_plot.values(),
                label=u"x = " + str(round(i, 2)) + " f(x) = " + str(round(hermite_plot[i], 2)), color='b')

y0 = []
y1 = []
y2 = []
for i in range(0, len(plot_x)):
    for j in range(0, 3):
        if j == 0:
            y0.append(f(plot_x[i]))
        elif j == 1:
            y1.append(f1(plot_x[i]) / 2)
        elif j == 2:
            y2.append(f2(plot_x[i]) / 6)
        else:
            break

for i in y0:
    print(i)
# plt.plot(func_plot_int_inc.keys(), y0, label=u'y', color='g')
print("------------")

for i in y1:
    print(i)
plt.plot(func_plot_int_inc.keys(), y1, label=u'y', color='g')
print("------------")
for i in y2:
    print(i)
plt.plot(func_plot_int_inc.keys(), y2, label=u'y', color='g')

plt.legend()
plt.show()
