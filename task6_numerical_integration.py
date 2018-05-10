import mpmath


def f(x):
    return (x * mpmath.coth(x)) / ((x ** 3) + 2 * x + 1)



