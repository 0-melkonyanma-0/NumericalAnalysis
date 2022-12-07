import math


def f1(x):
    return math.log(math.sin(1/x**2))


def f1_interval():
    return [1, 2]


def f2(x):
    return (x**2)*(math.sin(1/x**2))


def f2_interval():
    return [1, 2]
