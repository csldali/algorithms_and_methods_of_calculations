import math
import numpy as np


# -------------------------------------------------Functions area-------------------------------------------------------


def function(x):
    return (1 / (x + 1)) - math.log(x, 10)


def function1(x):
    return -(1 / ((x + 1) ** 2)) - (1 / (x * np.log(x)))


# -------------------------------------------------End of functions area------------------------------------------------


x_left = 1
x_right = 5
eps = 0.005

# ------------------------------------------------half_divide_method----------------------------------------------------

x = (x_left + x_right) / 2
while math.fabs(function(x)) > eps:
    x = (x_left + x_right) / 2
    x_left, x_right = (x_left, x) if function(x_left) * function(x) < 0 else (x, x_right)

print("half_divide_method:\nx: " + str(x) + "\tf(x): " + str(function(x)))

# ------------------------------------------------end_of_half_divide_method---------------------------------------------

x_left = 1
x_right = 5
eps = 0.005

# ------------------------------------------------newtons_method--------------------------------------------------------

x0 = (x_left + x_right) / 2
x1 = x0 - (function(x0) / function1(x0))
while math.fabs(x1 - x0) > eps:
    x0 = x1
    x1 = x0 - (function(x0) / function1(x0))

print("newtons_method:\nx: " + str(x0) + "\tf(x): " + str(function(x0)))

# ------------------------------------------------end_of_newtons_method-------------------------------------------------
