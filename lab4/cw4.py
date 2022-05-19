from random import *
from pylab import figure, cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def vector_dif(x, y):
    out = list()
    for i in range(len(x)):
        out.append(x[i] - y[i])
    return out


def vector_mult(x, y):
    for i in range(len(x)):
        x[i] = x[i] * y


def f1(x1, x2, x3):
    return 2.0 * pow(x1, 2) + 2.0 * pow(x2, 2) + pow(x3, 2) - 2.0 * x1 * x2 - 2.0 * x2 * x3 - 2.0 * x1 + 3.0


def f2(x1, x2):
    return 3.0 * pow(x1, 4) + 4.0 * pow(x1, 3) - 12.0 * pow(x1, 2) + 12.0 * pow(x2, 2) - 24.0 * x2


def p1_x1(vec) -> float:
    return 4.0 * vec[0] - 2.0 * vec[1] - 2.0


def p1_x2(vec) -> float:
    return 4.0 * vec[1] - 2.0 * vec[0] - 2.0 * vec[2]


def p1_x3(vec) -> float:
    return 2.0 * vec[2] - 2.0 * vec[1]


def p2_x1(vec) -> float:
    return round(12.0 * pow(vec[0], 3) + 12.0 * pow(vec[0], 2) - 24.0 * vec[0], 5)


def p2_x2(vec) -> float:
    return 24.0 * vec[1] - 24.0


def gradient_function_1(c, e, range_n, losowe=False):
    flag = True
    if losowe:
        x_old = [randrange(-range_n, range_n, 1) for i in range(3)]
        print("\nDla wartosci losowych: \n")
    else:
        x_old = [1.0, 1.0, 1.0]
        print("\nDla wartosci stalych: \n")

    x_new = [0.0 for i in range(3)]

    while flag:
        x_new[0] = float(x_old[0] - c * p1_x1(x_old))
        x_new[1] = float(x_old[1] - c * p1_x2(x_old))
        x_new[2] = float(x_old[2] - c * p1_x3(x_old))
        maximum = 0.0
        for i in range(3):
            a = (abs(x_new[i] - x_old[i]))
            if a > maximum:
                maximum = a
        if maximum < e:
            print('Minimum funckcji 1 \nx1: {:0.2f}, \nx2: {:0.2f}, \nx3: {:0.2f} \nwartosc: {:0.2f}\n'.format(x_new[0], x_new[1], x_new[2],
                                                                                       f1(x_new[0], x_new[1],
                                                                                          x_new[2])))
            flag = False
        x_old = x_new.copy()


def gradient_function_2(c, e, range_n, losowe=False):
    flag = True
    if losowe:
        x_old = [randrange(-range_n, range_n, 1) for i in range(2)]
        print("\nDla wartosci losowych: \n")
    else:
        x_old = [1.0, 1.0]
        print("\nDla wartosci stalych: \n")


    x_new = [0.0 for i in range(2)]

    while flag:
        x_new[0] = float(x_old[0] - c * p2_x1(x_old))
        x_new[1] = float(x_old[1] - c * p2_x2(x_old))
        maximum = 0.0
        for i in range(2):
            a = (abs(x_new[i] - x_old[i]))
            if a > maximum:
                maximum = a
        if maximum < e:
            print('Minimum funkcji 2 \nx1: {:0.2f}, \nx2: {:0.2f}, \nwartosc: {:0.2f}'.format(x_new[0], x_new[1],
                                                                         f2(x_new[0], x_new[1]
                                                                            )))
            flag = False
        x_old = x_new.copy()


if __name__ == '__main__':
    print("Laboratoria 4 \n")

    n1 = 100
    c1 = 0.01
    e1 = 0.000001
    gradient_function_1(c1, e1, n1, losowe=False)
    gradient_function_2(c1, e1, n1, losowe=False)
    gradient_function_1(c1, e1, n1, losowe=True)
    try:
        gradient_function_2(c1, e1, n1, losowe=True)
    except OverflowError:
        print("Overflow Error w losowej funkcji 2")
    # gradient_function_2(c1, e1, n1, losowe=True)


    # main_loop(c1, e1, 50, n1)
