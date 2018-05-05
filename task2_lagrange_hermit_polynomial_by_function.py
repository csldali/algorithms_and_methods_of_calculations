import matplotlib.pyplot as plt
import numpy as np
import math
import sympy
from pylab import *

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



def f(x):
    return math.cos(x) / (1 + (math.cos(x) ** 2))


def f1(x):
    return sin(x) * ((cos(x) ** 2) - 1) * (((cos(x) ** 2) + 1) ** -2)


def f2(x):
    return cos(x) * (((cos(x) ** 2) + 1) ** -3) * (2 * cos(x) ** 2 * sin(x) ** 2 - 6 * sin(x) ** 2 + cos(x) ** 4 - 1)


def divided_differences(x_array, y_array):
    y_array_buf = []
    delta = 1
    print("|------------------")
    while True:
        if len(y_array_buf) != 0 or len(y_array) != 0:
            for i in np.arange(0, len(y_array), 1):
                print(str(i) + ") f" + str(delta) + "(x): " + str(y_array[i]))
            for i in np.arange(0, len(y_array), 1):
                if i != (len(y_array) - 1):
                    if (x_array[i + delta] - x_array[i]) == 0:
                        y_array_buf.append(0)
                    else:
                        y_array_buf.append((y_array[i + 1] - (y_array[i])) / (x_array[i + delta] - x_array[i]))
                else:
                    print("|------------------")
                    break
            y_array.clear()
            delta += 1
            for i in np.arange(0, len(y_array_buf), 1):
                print(str(i) + ") f" + str(delta) + "(x): " + str(y_array_buf[i]))

            for i in np.arange(0, len(y_array_buf), 1):
                if i != (len(y_array_buf) - 1):
                    if (x_array[i + delta] - x_array[i]) == 0:
                        y_array.append(0)
                    else:
                        y_array.append((y_array_buf[i + 1] - (y_array_buf[i])) / (x_array[i + delta] - x_array[i]))
                else:
                    print("|------------------")
                    break
            y_array_buf.clear()
            delta += 1
        else:
            break


def hermitePol(x):
    return -0.5 + 0.3183098861837907 * (x + math.pi) - 0.10132118364233778 * (
            (x + math.pi) * x) + 0.03225153443319949 * ((x + math.pi) * (x ** 2)) - 0.010265982254684336 * (
                   (x + math.pi) * (x ** 3))


###########################the end of functions area################################################################

a = -math.pi
b = math.pi
n = 5

print(f(-math.pi))

print(f(0))
print(f(math.pi))

print("--------------------------------------------")

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
    hermite_plot[correct_index(a, b, n, i)] = hermitePol(correct_index(a, b, n, i))

# Plot construction
fig = plt.gcf()
fig.canvas.set_window_title('Plot construction')
plt.grid(True)
plt.title(u'Plots')
plt.xlabel(u'Argument [x]')
plt.ylabel(u'Function [f(x)]')

plt.plot(func_plot_small_inc.keys(), func_plot_small_inc.values(), label=u'Main plot', color='k')


plt.plot(lagrange_plot.keys(), lagrange_plot.values(), label=u'The Lagrange plot',
         color='r', ls="--")

x = [-math.pi, 0, 0, 0, math.pi]
y = [-0.5, 0.5, 0.5, 0.5, -0.5]

divided_differences(x, y)
plt.plot(hermite_plot.keys(), hermite_plot.values(), label=u'The Hermite plot', color='m')

lagrange_plot.clear()
for i in np.arange(0, n + 1, 1):
    lagrange_plot[correct_index(a, b, n, i)] = lagrange(plot_x, plot_y, correct_index(a, b, n, i), n)


for i in lagrange_plot:
    plt.scatter(lagrange_plot.keys(), lagrange_plot.values(),
                label=u"Lagrange x = " + str(round(i, 2)) + " f(x) = " + str(round(lagrange_plot[i], 2)), color='r')

hermite_plot.clear()
for i in np.arange(0, n + 1, 1):
    hermite_plot[correct_index(a, b, n, i)] = hermitePol(correct_index(a, b, n, i))

for i in lagrange_plot:
    plt.scatter(lagrange_plot.keys(), lagrange_plot.values(),
                label=u"Hermite x = " + str(round(i, 2)) + " f(x) = " + str(round(lagrange_plot[i], 2)), color='m')

plt.legend()
plt.show()
