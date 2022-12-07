from _Data import getDataSet
from additional_info import PATH, PATH1
from os import system
import pprint
from NewtonFormulas import first_newton, second_newton
from GaussFormulas import first_gauss, second_gauss
# function is 1+e^x
# mypolinom x^9+1.5^x^6+x^2-sin(arccos(x))
# x**9+1.5*x**6+x**2-math.sin(math.acos(x))


def main():
    nodes = getDataSet(path=PATH)
    x = [i.x for i in nodes]
    y = [i.f for i in nodes]
    diff_table = list([y])
    diff_nf = [y[0]]
    diff_nb = [y[-1]]
    diff_gf = [y[int(len(nodes)/2)]]
    diff_gb = [y[int(len(nodes)/2)]]

    for i in range(len(nodes)-1):
        temp_diff = []
        for j in range(len(diff_table[i])-1):
            temp_diff.append(diff_table[i][j+1]-diff_table[i][j])
        diff_table.append([round(i, 3) for i in temp_diff])
        diff_nf.append(round(temp_diff[0], 3))
        diff_nb.append(round(temp_diff[-1], 3))

    for i in range(1, len(nodes)):
        diff_gf.append(diff_table[i][int((len(nodes)-i)/2)])

        if i % 2 == 1:
            diff_gb.append(diff_table[i][int((len(nodes)-i)/2)-1])
        else:
            diff_gb.append(diff_table[i][int((len(nodes)-i)/2)])

    print(round(first_gauss(nodes=nodes, diff_table=diff_gf, int_point=1), 3))
    print(round(second_gauss(nodes=nodes, diff_table=diff_gb, int_point=1), 3))
    print(round(first_newton(nodes=nodes, diff_table=diff_nf, int_point=1), 3))
    print(round(second_newton(nodes=nodes, diff_table=diff_nb, int_point=1), 3))


if __name__ == '__main__':
    system('clear')
    main()
