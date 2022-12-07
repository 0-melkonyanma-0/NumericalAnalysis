import math
from _init_ import *

eps = 0
inter_point = 0


def inputData() -> None:
    global eps, inter_point

    try:
        eps = float(input("Enter error : "))
        if eps > 1 or eps < 0:
            print('\n\tError more than 1 or less than 0!!\n')
            inputData()
            return
        inter_point = float(input("Enter interpolation point : "))
        if inter_point > 2 or inter_point < 1:
            print('\n\tInterpolation point more than 2 or less than 1!\n')
            inputData()
            return

    except (KeyboardInterrupt):
        print('\n\tProgramm close.\n')
        exit()
    except (ValueError):
        print("\n\tIt is not a number.\n")
        inputData()


def menu() -> None:
    global eps, inter_point
    try:
        choice = int(input("Menu item : "))
        if choice < 1 or choice > 2:
            print("\n\tThere is no such menu item.\n")
            menu()
        if choice == 1:
            eps = 1e-3
            inter_point = 1.43
        if choice == 2:
            inputData()
    except (ValueError):
        print("\n\tIt is not a number.\n")
        menu()
    except (KeyboardInterrupt):
        print('\n\n\tProgramm close.\n')
        exit()


print('1.Default values (eps = 1e-3, inter_point = 1.43).\n2.Enter values.\n')
menu()

print('\n')

time_start = time()
lagrange_res = Lagrange(nodes, inter_point)
time_end = time() - time_start
print('Result Lagrange: ', lagrange_res)
print('Time (sec.) : ', time_end)

print('\n')

time_start = time()
aitken_res = AitkenScheme(nodes, inter_point, eps)
time_end = time() - time_start

precision = len(str(eps))

print('Result Aitken sheme: ', round(aitken_res, precision))
print('Time (sec.) : ', time_end)
print(f'\ne^{inter_point} =', math.e**inter_point)

Draw_Graph(inter_point, aitken_res, nodes)
