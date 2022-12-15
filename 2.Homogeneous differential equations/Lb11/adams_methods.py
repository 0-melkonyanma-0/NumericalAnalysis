
import numpy as np
from scipy.optimize import fsolve
from method_runge_kutta_3nd import method_runge_kutta
from exact_solution import getX

step_N = 9
h = 1/step_N
i = 0
list_x = getX(step_N)
y = method_runge_kutta(list_x, h, 2)


def adams_method_explicit(list_x, y: list, h):

    for i in range(len(list_x)-3):
        y.append(y[i+2]+h/12*(23*(list_x[i+2]**2+y[i+2])-16 *
                 (list_x[i+1]**2+y[i+1])+5*(list_x[i]**2+y[i])))

    return y


def adams_method_non_explicit():
    global i
    for i in range(len(list_x)-2):
        y.append(fsolve(myFunc, y[i+1])[0])
    return y


def myFunc(y_):
    global i, list_x, y

    y__ = y[i+1]+h/12*(5*(list_x[i+2]**2+y_) + 8 *
                       (list_x[i+1]**2+y[i+1])-(list_x[i]**2+y[i])) - y_
    return y__
