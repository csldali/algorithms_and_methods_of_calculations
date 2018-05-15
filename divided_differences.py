import numpy as np


#################################functions area#####################################################################
# The function given by task
def function(x):
    return ((2 * x) ** 3) - ((2 * x) ** 2) + (3 * x) - 1
    # return 1 / (1 + x ** 2)


def finite_differences(y_array):
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


def divided_differences(x_array, y_array):
    y_array_buf = []
    delta = 1
    print("|------------------")
    while True:
        if len(y_array_buf) != 0 or len(y_array) != 0:
            for i in np.arange(0, len(y_array), 1):
                print(str(i) + ") f" + str(delta) + "(x): " + str(y_array[i]))
            for i in np.arange(0, len(y_array), 1):
                if i != (len(y_array) - 1):
                    y_array_buf.append((y_array[i + 1] - (y_array[i])) / (x_array[i + delta] - x_array[i]))
                else:
                    print("|------------------")
                    break
            y_array.clear()
            delta += 1
            for i in np.arange(0, len(y_array_buf), 1):
                print(str(i) + ") f" + str(delta) + "(x): " + str(y_array_buf[i]))

            for i in np.arange(0, len(y_array_buf), 1):
                if i != (len(y_array_buf) - 1):
                    y_array.append((y_array_buf[i + 1] - (y_array_buf[i])) / (x_array[i + delta] - x_array[i]))
                else:
                    print("|------------------")
                    break
            y_array_buf.clear()
            delta += 1
        else:
            break


def div_by_arguments(x_array):
    y_array = []
    for i in x_array:
        y_array.append(function(i))
    return finite_differences(y_array)


#################################end_of_functions area##################################################################


print("\ndivided_differences:")
x_array = [1, 1.2, 1.3, 1.5, 1.8]
y_array = [1.54, 1.562, 1.567, 1.571, 1.573]
divided_differences(x_array, y_array)

print("\nfinite_differences:")
y_array = [62, 12, 2, 6, 32]
finite_differences(y_array)
