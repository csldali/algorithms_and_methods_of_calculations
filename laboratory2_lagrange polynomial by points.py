import matplotlib.pyplot as plt
import numpy as np


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


###########################the end of functions area################################################################

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
for x in range(0, len(array_x), 1):
    lagrangePlotData[array_x[x]] = lagrange(array_x, array_y_fx, array_x[x], count)
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

plt.plot(lagrangePlotData.keys(), lagrangePlotData.values(), label=u'The Lagrange plot with inc. in 1', color='r',
         ls='--')
plt.scatter(lagrangePlotData.keys(), lagrangePlotData.values(), label=u'Lagrange interpolation points:', color='g')

for i in lagrangePlotData:
    plt.scatter(lagrangePlotData.keys(), lagrangePlotData.values(),
                label=u"x = " + str(i) + " f(x) = " + str(round(lagrangePlotData[i], 3)), color='g')
plt.legend()
plt.show()
