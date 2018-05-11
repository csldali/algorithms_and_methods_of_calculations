import mpmath
import numpy
from scipy import integrate


def f(x):
    return (x * mpmath.coth(x)) / ((x ** 3) + 2 * x + 1)


func = lambda x: (x * mpmath.coth(x)) / ((x ** 3) + 2 * x + 1)


def trapezoidal_formula(a, b, n):
    n = n
    h = (b - a) / n
    x = []
    for i in numpy.arange(a, b + h / 2, h):
        x.append(i)
    res = f(x[0])
    # for i in range(0, n):
    for i in range(1, n):
        # res = res + (f(1 + h * i) + f(1 + h * (1 + i)))
        res = res + (2 * f(x[i]))
    # res = (h / 2) * res
    res = res * ((b - a) / (2 * n))
    print("trapezoidal_formula for n =", n, ":\t", round(res, 6))


def left_rectangles(a, b, n):
    n = n
    h = (b - a) / n
    x = []
    for i in numpy.arange(a, b + h / 2, h):
        x.append(i)
    res = 0
    for i in range(0, n - 1):
        res = res + f(x[i])
    res = h * res
    print("left_rectangles for n =", n, ":\t", round(res, 6))


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
