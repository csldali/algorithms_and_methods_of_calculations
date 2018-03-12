# Functions
def function(x):
    return x ** 3 - (2 * x) + 3


########################################

print("Enter the x0:")
x0 = float(input())

print("Enter the x1:")
x1 = float(input())

print("Enter the epsilon (0.001):")
e = float(input())

xNext = 0.0
xCurr = x1
xPrev = x0
buf = 0.0

while True:
    buf = xNext
    xNext = xCurr - function(xCurr) * (xPrev - xCurr) / (function(xPrev) - function(xCurr))
    xPrev = xCurr
    xCurr = buf

    if abs(xNext - xCurr) > e:
        # print("Answer: " + str(round(xNext, 3)))
        print("Answer: " + str(xNext) + "\nF(x): " + str(function(xNext)))
        break
