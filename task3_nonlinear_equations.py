import math


# -------------------------------------------------Functions area-------------------------------------------------------


def my_function(x):
    return (1 / (x + 1)) - math.log10(x)


# -------------------------------------------------End of functions area------------------------------------------------


# ------------------------------------------------Method of division in half--------------------------------------------


x_left = -20
x_right = 20
eps = 0.005

if my_function(x_left) == 0:
    print("The root of the equation\t" + x_left)
elif my_function(x_right):
    print("The root of the equation\t" + x_right)

while x_right - x_left > eps:
    dx = (x_right - x_left) / 2
    x[i] = x[i] + dx
