import matplotlib.pyplot as plt
from exact_solution import getX, exact_solution
from method_runge_kutta_3nd import method_runge_kutta
from adams_methods import adams_method_explicit, adams_method_non_explicit
import math


def main():
    step_N = 9
    h = 1/step_N
    list_x = getX(step_N)
    list_y = exact_solution(list_x)
    y_prepare = method_runge_kutta(list_x, h, 3)
    y_explicit = adams_method_explicit(list_x, y_prepare, h)
    y_non_explicit = adams_method_non_explicit()

    for i in range(len(y_explicit)):
        print(
            f'|explicit({i}) - non_explicit({i})| = {math.fabs(y_explicit[i]-y_non_explicit[i])}')

    plt.grid()
    plt.plot(list_x, list_y)

    plt.plot(list_x, y_explicit)
    plt.plot(list_x, y_non_explicit)

    plt.legend(['Точное', 'Метод Адамса Явный', 'Метод Адамса Неявный'])
    plt.show()


if __name__ == "__main__":
    main()
