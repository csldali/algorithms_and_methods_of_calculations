import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


# Functions
def function(x):
    return x ** 3 - (2 * x) + 3

#########################################


a = -2.5
b = -1.5

c = (a + b) / 2.0

if (function(a) * function(c)) < 0.0:
    b = c
elif (function(c) * function(b)) < 0.0:
    a = c

while True:

    if abs(a - b) < 0.0001:
        # if(abs(function(c)) == 0.0):
        print("F(x) = " + str(c))
        break
    else:
        c = (a + b) / 2.0

        if (function(a) * function(c)) < 0.0:
            b = c
        elif (function(c) * function(b)) < 0.0:
            a = c
