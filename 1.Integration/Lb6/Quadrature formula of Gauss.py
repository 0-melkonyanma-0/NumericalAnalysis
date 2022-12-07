from _Function import f1 as f, f1_interval as f_interval
from additional_info import w, t
import os


def main():
    os.system('clear')

    eps = 1e-3
    a = f_interval()[0]
    b = f_interval()[1]
    i_p = 0
    i_n = 0

    for i in range(len(w)):
        integral = 0
        for j in range(len(w[i])):
            integral += w[i][j]*f(0.5*(a+b+t[i][j]*(b-a)))

        i_n = (0.5*(b-a)*integral)

        if i >= 1:
            diff = abs(i_n-i_p)
            print(f'Difference |I{i+1} - I{i}| = {diff}.')

            if diff < eps:
                print(f'n = {i+1}, Integral = {i_n}')
                break

        i_p = i_n


if __name__ == '__main__':
    main()
