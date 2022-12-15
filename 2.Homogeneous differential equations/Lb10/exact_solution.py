import math


def getX(h) -> list:
    list_x = []
    i = 0
    while i <= 1+h:
        list_x.append(round(i, 3))
        i += h
    return list_x


def exact_solution(list_x) -> list:

    list_y = []

    for i in list_x:
        list_y.append(round(math.exp(2*i), 3))

    return list_y
