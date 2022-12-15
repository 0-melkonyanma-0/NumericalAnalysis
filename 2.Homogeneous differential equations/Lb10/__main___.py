# u'' = 4u 0 < x <= 1 u(0) = 1 u'(0) = 2
# let z = u'
# then we get   u' = z
#               z' = 4u
#               u(0) = 1 z(0) = 2
#
#              THIRD ORDER RUNGE-KUTTA METHOD
#
#              k1 = f(x0,y0,z0)*delta
#              m1 = g(x0,y0,z0)*delta
#              k2 = f(x0 + delta/2,y0 + k1/2,z0 + m1/2)*delta
#              m2 = g(x0 + delta/2,y0 + k1/2,z0 + m1/2)*delta
#              k3 = f(x0 + delta,y0 + 2*k2 - k1,z0 + 2*m2 - m1)*delta
#              m3 = g(x0 + delta,y0 + 2*k2 - k1,z0 + 2*m2 - m1)*delta
#
#              z_n+1 = y_n+1 = zn + 1/6[m1 + 4m2 + m3] or yn + 1/6 *[k1 + 4k2 + k3]


import matplotlib.pyplot as plt
from exact_solution import getX, exact_solution
from runge_kutta_3rd_approximation import method_runge_kutta
from math import fabs, log2
import os


def main():
    h = 1/10
    list_x = getX(h)
    list_y = exact_solution(list_x)  # 0.1 1.221
    y = method_runge_kutta(list_x, h)
    diff_1 = [fabs(list_y[i] - y[i]) for i in range(len(list_x))]
    diff_1 = max(diff_1)
    h /= 2
    list_x_2 = getX(h)
    list_y_2 = exact_solution(list_x_2)
    y_ = method_runge_kutta(list_x_2, h)

    diff_2 = [fabs(list_y_2[i] - y_[i]) for i in range(len(list_x_2))]
    diff_2 = max(diff_2)

    k = log2(diff_1/diff_2)
    os.system('clear')
    print('Порядок : ', round(k, 2))
    plt.plot(list_x, list_y)
    plt.plot(list_x, y)
    plt.legend(['Точное', 'Метод Рунге-Кутты'])
    plt.show()


if __name__ == "__main__":
    main()
