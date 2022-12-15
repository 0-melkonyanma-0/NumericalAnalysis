# u'' = x**2 0 < x <= 1 u(0) = 1 u'(0) = 0
import math
import matplotlib.pyplot as plt
from dfm import dfm_method
from exact_solution import getX, exact_solution


def main():
    step_N = 100

    list_x = getX(step_N)
    list_y = exact_solution(list_x)

    dfm_y = dfm_method(list_x, 1/step_N)
    plt.grid()
    plt.plot(list_x, list_y)
    plt.plot(list_x, dfm_y)
    plt.scatter(list_x, dfm_y)

    plt.legend(['Точное', 'Рзаностная схема'])
    plt.show()


if __name__ == "__main__":
    main()
