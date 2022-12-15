import math


def getX(step) -> list:
    list_x = []
    i = 0
    while i <= 1:
        list_x.append(i)
        i += 1/step
    return list_x


def exact_solution(list_x) -> list:

    list_y = []

    for i in list_x:
        list_y.append(round(i**4/12+1, 3))
        #
    return list_y
