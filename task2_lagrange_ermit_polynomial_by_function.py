import matplotlib.pyplot as plt
import numpy as np
import math as math


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


def math_function1(x):
    return np.diff(x)


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


# значение ф-ции == значению производной этой фунции
# The function of the algorithm for finding the Lagrange polynomial
def ermit(x):
    return 0


###########################the end of functions area################################################################

a = -math.pi * 2
b = math.pi * 2
n = 5

func_plot_small_inc = main_plot(a, b, n)
func_plot_int_inc = get_points(a, b, n)
plot_x = []
plot_y = []

for key, value in func_plot_int_inc.items():
    plot_x.append(key)
    plot_y.append(value)

lagrange_plot = {}

for i in np.arange(0, n + 0.01, 0.01):
    lagrange_plot[correct_index(a, b, n, i)] = lagrange(plot_x, plot_y, correct_index(a, b, n, i), n)


print()

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
         color='g', ls="--")

lagrange_plot.clear()
for i in np.arange(0, n + 1, 1):
    lagrange_plot[correct_index(a, b, n, i)] = lagrange(plot_x, plot_y, correct_index(a, b, n, i), n)

for i in lagrange_plot:
    plt.scatter(lagrange_plot.keys(), lagrange_plot.values(),
                label=u"x = " + str(round(i, 2)) + " f(x) = " + str(round(lagrange_plot[i], 2)), color='r')

plt.legend()
plt.show()
