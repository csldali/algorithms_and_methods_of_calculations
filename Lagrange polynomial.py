import matplotlib.pyplot as plt
import numpy as np


# The function of the algorithm for finding the Lagrange polynomial
def lagrange(array_x_arguments, array_y_function, x_argument, array_len):
    lagrange_x = 0.0
    p = 1.0
    for i in range(0, array_len, 1):
        for j in range(0, array_len, 1):
            if i != j:
                p *= (x_argument - array_x_arguments[j]) / (array_x_arguments[i] - array_x_arguments[j])
        lagrange_x += p * array_y_function[i]
        p = 1
    return lagrange_x


while True:
    count = int(input("Enter the count of elements (by default: i = 4): ") or 4)
    if count <= 0:
        print("Can not be 0 or under 0. Try again...")
    else:
        break

print("Enter the each x(i) (after each element -> press \"Enter\")")
array_x = []
for i in range(0, count, 1):
    array_x.append(float(input()))

print("Enter the each F(i) (after each element -> press \"Enter\")")
array_y_fx = []
for j in range(0, count, 1):
    array_y_fx.append(float(input()))

# Forming the plot by given points
mainPlotData = {}
for i in range(0, len(array_x)):
    mainPlotData[array_x[i]] = array_y_fx[i]

# Forming the Lagrange plot
print("-------------------------")
print("|        Result         |")
print("-------------------------")
lagrangePlotData = {}
for x in range(0, count + 2, 1):
    lagrangePlotData[x] = lagrange(array_x, array_y_fx, x, count)
    print("|\tx = {0},\tF(x) = {1:.1f}\t|".format(x, lagrange(array_x, array_y_fx, x, count)))
print("-------------------------")

mainPlotData_small_inc = {}
for i in np.arange(0, float(count) + 1.0, 0.01):
    mainPlotData_small_inc[i] = lagrange(array_x, array_y_fx, i, count)

# Plot construction
fig = plt.gcf()
fig.canvas.set_window_title('Plot construction')
plt.grid(True)
plt.title(u'Plots')
plt.xlabel(u'Argument [x]')
plt.ylabel(u'Function [f(x)]')

plt.plot(mainPlotData.keys(), mainPlotData.values(), label=u'Main plot', color='b')
plt.plot(mainPlotData_small_inc.keys(), mainPlotData_small_inc.values(), label=u'The Lagrange plot with inc. in 0.01',
         color='c')
plt.plot(lagrangePlotData.keys(), lagrangePlotData.values(), label=u'The Lagrange plot with inc. in 1', color='r')
plt.scatter(lagrangePlotData.keys(), lagrangePlotData.values(), label=u'Lagrange interpolation points:', color='g')

for i in lagrangePlotData:
    plt.scatter(lagrangePlotData.keys(), lagrangePlotData.values(),
                label=u"x = " + str(i) + " f(x) = " + str(round(lagrangePlotData[i], 3)), color='g')
plt.legend()
plt.show()
