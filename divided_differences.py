import numpy as np


#################################functions area#####################################################################
# The function given by task
def function(x):
    return ((2 * x) ** 3) - ((2 * x) ** 2) + (3 * x) - 1
    # return 1 / (1 + x ** 2)


def div_by_point(y_array):
    y_array_buf = []
    delta = 0
    print("|------------------")
    while True:
        if len(y_array_buf) != 0 or len(y_array) != 0:
            for i in np.arange(0, len(y_array), 1):
                print(str(i) + ") f" + str(delta) + "(x): " + str(y_array[i]))
            for i in np.arange(0, len(y_array), 1):
                if i != (len(y_array) - 1):
                    y_array_buf.append(y_array[i + 1] - y_array[i])
                else:
                    print("|------------------")
                    break
            y_array.clear()
            delta += 1
            for i in np.arange(0, len(y_array_buf), 1):
                print(str(i) + ") f" + str(delta) + "(x): " + str(y_array_buf[i]))

            for i in np.arange(0, len(y_array_buf), 1):
                if i != (len(y_array_buf) - 1):
                    y_array.append(y_array_buf[i + 1] - y_array_buf[i])
                else:
                    print("|------------------")
                    break
            y_array_buf.clear()
            delta += 1
        else:
            break


def div_by_function(x_array):
    y_array = []
    for i in x_array:
        y_array.append(function(i))
    y_array_buf = []
    delta = 0
    print("|------------------")
    while True:
        if len(y_array_buf) != 0 or len(y_array) != 0:
            for i in np.arange(0, len(y_array), 1):
                print(str(i) + ") f" + str(delta) + "(x): " + str(y_array[i]))
            for i in np.arange(0, len(y_array), 1):
                if i != (len(y_array) - 1):
                    y_array_buf.append(y_array[i + 1] - y_array[i])
                else:
                    print("|------------------")
                    break
            y_array.clear()
            delta += 1
            for i in np.arange(0, len(y_array_buf), 1):
                print(str(i) + ") f" + str(delta) + "(x): " + str(y_array_buf[i]))

            for i in np.arange(0, len(y_array_buf), 1):
                if i != (len(y_array_buf) - 1):
                    y_array.append(y_array_buf[i + 1] - y_array_buf[i])
                else:
                    print("|------------------")
                    break
            y_array_buf.clear()
            delta += 1
        else:
            break


#################################end_of_functions area##################################################################


print("By points:")
y_array = [62, 12, 2, 6, 32]
div_by_point(y_array)



print("\n\n\nBy function:")
x_array = [0, 1, 2, 3, 4, 5]
div_by_function(x_array)


print("\n\n\nBy wiki function:")
x_array = [0, 1, 2, 3, 4, 5]
div_by_function(x_array)
