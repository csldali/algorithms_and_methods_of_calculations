import math
import numpy as np


# -------------------------------------------------Functions area-------------------------------------------------------


def function(x):
    return (1 / (x + 1)) - math.log(x, 10)


def function1(x):
    return -(1 / ((x + 1) ** 2)) - (1 / (x * np.log(x)))


f = lambda x: (1 / (x + 1)) - math.log(x, 10)
f1 = lambda x: -(1 / ((x + 1) ** 2)) - (1 / (x * np.log(x)))


def half_divide_method(a, b, e, f):
    x = (a + b) / 2
    while math.fabs(f(x)) >= e:
        x = (a + b) / 2
        a, b = (a, x) if f(a) * f(x) < 0 else (x, b)
    return x


def newtons_method(a, b, e, f, f1):
    x0 = (a + b) / 2
    x1 = x0 - (f(x0) / f1(x0))
    while True:
        if math.fabs(x1 - x0) < e: return x1
        x0 = x1
        x1 = x0 - (f(x0) / f1(x0))


# -------------------------------------------------End of functions area------------------------------------------------


x_left = 1
x_right = 30
eps = 0.005

# ------------------------------------------------half_divide_method----------------------------------------------------
print("half_divide_method:\tx: " + str(half_divide_method(x_left, x_right, eps, f)) + "\tf(x): " + str(
    function(half_divide_method(x_left, x_right, eps, f))))

x = (x_left + x_right) / 2
while math.fabs(function(x)) >= eps:
    x = (x_left + x_right) / 2
    x_left, x_right = (x_left, x) if function(x_left) * function(x) < 0 else (x, x_right)

print("half_divide_method:\tx: " + str(x) + "\tf(x): " + str(function(x)))

# ------------------------------------------------end_of_half_divide_method---------------------------------------------

x_left = 1.0
x_right = 5.0
eps = 0.005

# ------------------------------------------------newtons_method--------------------------------------------------------
print("newtons_method:\t x: " + str(newtons_method(x_left, x_right, eps, f, f1)) + "\tf(x): " + str(
    function(newtons_method(x_left, x_right, eps, f, f1))))
x0 = (x_left + x_right) / 2
x1 = x0 - (function(x0) / function1(x0))
while math.fabs(x1 - x0) > eps:
    x0 = x1
    x1 = x0 - (function(x0) / function1(x0))

print("newtons_method:\tx: " + str(x1) + "\tf(x): " + str(function(x1)))

# ------------------------------------------------end_of_newtons_method-------------------------------------------------
