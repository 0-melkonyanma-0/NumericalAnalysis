import math


def getX(step) -> list:
    list_x = []
    i = 0
    while i <= 2+1/step:

        list_x.append(round(i, 3))
        i += 1/step
    return list_x


def exact_solution(list_x) -> list:

    list_y = []

    for i in list_x:
        list_y.append(round(56/27*math.exp(3*i)-1/3*i-2/9*i-2/27, 3))

    return list_y
