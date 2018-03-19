import matplotlib.pyplot as plt
import numpy as np
import math as math


#################################functions area#####################################################################

# The function of the algorithm for finding the Lagrange polynomial
def lagrange(array_x_arguments, array_y_function, x_argument):
    lagrange_x = 0.0
    p = 1.0
    for i in range(0, len(array_x_arguments), 1):
        for j in range(0, len(array_x_arguments), 1):
            if i != j:
                p *= (x_argument - array_x_arguments[j]) / (array_x_arguments[i] - array_x_arguments[j])
        lagrange_x += p * array_y_function[i]
        p = 1
    return lagrange_x


# Counting of step for each point and the function
def func(a, b, n):
    def f(x):
        return (math.cos(x)) / (1 + math.cos(x) ** 2)

    list_of_points = {}
    h = (b - a) / n
    for i in np.arange(0, n, 0.01):
        list_of_points[a + i * h] = f(i)
    return list_of_points


###########################the end of functions area################################################################


mp_i = float(input("Enter first point of interval: ") or -3.14)
p_i = float(input("Enter second point of interval: ") or 3.14)
n = int(input("Enter n: ") or 10)

func_plot = func(p_i, mp_i, n)
lagrange_plot_arguments = []
lagrange_plot_y = []

for key, value in func_plot.items():
    lagrange_plot_arguments.append(key)
    lagrange_plot_y.append(value)

print(lagrange_plot_arguments)
print(lagrange_plot_y)

lagrange_plot = {}
for i in func_plot:
    lagrange_plot[i] = lagrange(lagrange_plot_arguments,  lagrange_plot_y, i)


# Plot construction
fig = plt.gcf()
fig.canvas.set_window_title('Plot construction')
plt.grid(True)
plt.title(u'Plots')
plt.xlabel(u'Argument [x]')
plt.ylabel(u'Function [f(x)]')

plt.plot(func_plot.keys(), func_plot.values(), label=u'Main plot', color='b')
#plt.plot(lagrange_plot.keys(), lagrange_plot.values(), label=u'The Lagrange plot with inc. in 0.01',
     #    color='c')
"""
plt.plot(lagrangePlotData.keys(), lagrangePlotData.values(), label=u'The Lagrange plot with inc. in 1', color='r',
         ls='--')
plt.scatter(lagrangePlotData.keys(), lagrangePlotData.values(), label=u'Lagrange interpolation points:', color='g')

for i in lagrangePlotData:
    plt.scatter(lagrangePlotData.keys(), lagrangePlotData.values(),
                label=u"x = " + str(i) + " f(x) = " + str(round(lagrangePlotData[i], 3)), color='g')
                """
plt.legend()
plt.show()
