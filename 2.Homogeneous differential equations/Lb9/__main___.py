import matplotlib.pyplot as plt
from exact_solution import exact_solution, getX
from euler_methods import euler_method_non_explicit, euler_method_explicit


def main():
    # x_0 = 0
    # y_0 = 2
    step_N = 10
    step_N2 = 100

    list_x1 = []
    list_x1 = getX(step_N)
    list_x2 = []
    list_x2 = getX(step_N2)

    exact_sl_y = exact_solution(list_x2)
    euler_sl_y1 = euler_method_explicit(list_x1, step_N)
    euler_sl_y2 = euler_method_explicit(list_x2, step_N2)
    euler_sl_ynon1 = euler_method_non_explicit(list_x1, step_N)

    plt.plot(list_x2, exact_sl_y)
    plt.plot(list_x1, euler_sl_y1)
    plt.plot(list_x1, euler_sl_ynon1)
    plt.plot(list_x2, euler_sl_y2)

    plt.legend(
        ['Точное', f'Явный h = {1/step_N}',
            f'Неявный  h = {1/step_N}', f'Явный  h= {1/step_N2}']
    )
    plt.show()


if __name__ == '__main__':
    main()
