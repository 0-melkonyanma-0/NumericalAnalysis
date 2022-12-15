import math


def getX(step) -> list:
    list_x = []
    i = 0
    while i <= 1+1/step:
        list_x.append(round(i, 3))
        i += 1/step
    return list_x


def exact_solution(list_x) -> list:

    list_y = []

    for i in list_x:
        list_y.append(round(-i**2-2*i+3*math.exp(i)-2, 3))

    return list_y
