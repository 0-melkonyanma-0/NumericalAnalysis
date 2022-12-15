import os
from Function import f1, f2, f3, f4, f5
from Function import f1_interval, f2_interval, f3_interval, f4_interval, f5_interval
from SimpsonParabola_Rule import simpson_n, simpson_2n
from MidRectRule import mid_rect
from TrapezoidRule import trapezodial

eps = 1e-4


def run_rect(f_, a_: float, b_: float) -> list:
    err_list = [1]
    res_list = list()
    teta = 1/3
    i = 0

    while err_list[i] > eps:
        i += 1
        a = mid_rect(f=f_, a=a_, b=b_, n=i)
        b = mid_rect(f=f_, a=a_, b=b_, n=2*i)
        err_list.append(teta*abs(b-a))
        res_list.append(a)

    return [i, res_list[i-1]]


def run_trapezoid(f_, a_: float, b_: float) -> list:
    err_list = [1]
    res_list = list()
    teta = 1/3
    i = 0

    while err_list[i] > eps:
        i += 1
        a = trapezodial(f=f_, a=a_, b=b_, n=i)
        b = trapezodial(f=f_, a=a_, b=b_, n=2*i)
        err_list.append(teta*abs(b-a))
        res_list.append(a)

    return [i, res_list[i-1]]


def run_simpson(f_, a_: float, b_: float) -> list:
    err_list = [1]
    res_list = list()
    teta = 1/15
    i = 0

    while err_list[i] > eps:
        i += 1
        a = simpson_n(f=f_, a=a_, b=b_, n=i)
        b = simpson_2n(f=f_, a=a_, b=b_, n=i)
        err_list.append(teta*abs(b-a))
        res_list.append(a)

    return [i, res_list[i-1]]


if __name__ == '__main__':
    os.system('clear')

    a = f5_interval()[0]
    b = f5_interval()[1]

    rectang = run_rect(f5, a, b)
    print('\t\tRectangular (Middle) Rule\n')
    print(f'Number of splits - {rectang[0]}')
    print(f'Result of method - {rectang[1]}\n')

    trapezoid = run_trapezoid(f5, a, b)
    print('\t\t Trapezoid Rule\n')
    print(f'Number of splits - {trapezoid[0]}')
    print(f'Result of method - {trapezoid[1]}\n')

    simpson = run_simpson(f5, a, b)
    print('\t\tSimpson Rule\n')
    print(f'Number of splits - {simpson[0]}')
    print(f'Result of method - {simpson[1]}\n')
