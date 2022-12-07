from random import uniform
from os import system


def main():
    system('clear')
    interval = [[1, 2], [2, 4], [1, 5]]
    exprement = [1e4, 1e6, 1e8]
    integral_res = list()
    func_exp = [1, 0, 0]

    for i in range(3):
        summa = 0.0
        res = 1.0
        for k in range(3):
            if func_exp[k] == 0:
                res *= (interval[k][1] - interval[k][0])
                continue
            for j in range(int(exprement[i])):
                summa += (interval[k][0] + (interval[k][1] -
                                            interval[k][0])*uniform(0, 1))**func_exp[k]
            res *= (interval[k][1] - interval[k][0])*summa/int(exprement[i])
        integral_res.append(res)

    print('\t\t Calculation results : ')
    for i in range(len(integral_res)):
        print(f'I_{i+1} ~ {integral_res[i]}')

    print('\n\t\tDifference modules:')
    print(f'|I_1-I_2| = {abs(integral_res[0]-integral_res[1])}')
    print(f'|I_2-I_3| = {abs(integral_res[1]-integral_res[2])}')


if __name__ == '__main__':
    main()
