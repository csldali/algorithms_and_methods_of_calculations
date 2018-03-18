import math


def function(x):
    return x ** 3 - (2 * x) + 3


########################################

x0 = float(input("Enter the x0: "))

x1 = float(input("Enter the x1: "))

e = str(input("Enter the epsilon (0.001): "))

buf = e.split('.')
n = len(buf[1])

e = float(e)
x2 = 0.0

while function(x1) != 0.0:
    buf = x2
    x2 = x1 - function(x1) * (x0 - x1) / (function(x0) - function(x1))
    x0 = x1
    x1 = buf

fx = x2

if round(x2, n) > 0:
    x2 = round(x2, n) + e
elif round(x2, n) < 0:
    x2 = round(x2, n) - e

print("x: " + str(x2) + "\nF(x): " + str(function(fx)))
