import mpmath
import numpy
from scipy import integrate


def f(x):
    # return (x * mpmath.coth(x)) / ((x ** 3) + 2 * x + 1)
    # return 3
    return x


# func = lambda x: (x * mpmath.coth(x)) / ((x ** 3) + 2 * x + 1)
# func = lambda x: 3
func = lambda x: x


def trapezoidal_formula(a, b, n):
    n = n
    h = (b - a) / n
    x = []
    for i in numpy.arange(a, b + h / 2, h):
        x.append(i)
    y = []
    y.append(f(x[0]))
    for i in range(1, n):
        y.append((2 * f(x[i])))
    y.append(f(x[n]))
    res = sum(y) * ((b - a) / (2 * n))
    print("trapezoidal_formula for n =", n, ":\t", res)


def left_rectangles(a, b, n):
    n = n
    h = (b - a) / n
    x = []
    for i in numpy.arange(a, b + h / 2, h):
        x.append(i)
    y = []
    for i in range(0, n):
        y.append(f(x[i]))
    res = h * sum(y)
    print("left_rectangles for n =", n, ":\t", res, 6)


if __name__ == '__main__':
    a = 1
    b = 2
    trapezoidal_formula(a, b, 3)
    trapezoidal_formula(a, b, 5)
    trapezoidal_formula(a, b, 10)
    trapezoidal_formula(a, b, 15)
    trapezoidal_formula(a, b, 20)
    trapezoidal_formula(a, b, 30)
    print("\nscipy.integrate.quad" + str(integrate.quad(func, a, b)) + "\n")
    left_rectangles(a, b, 3)
    left_rectangles(a, b, 5)
    left_rectangles(a, b, 10)
    left_rectangles(a, b, 15)
    left_rectangles(a, b, 20)
    left_rectangles(a, b, 30)
