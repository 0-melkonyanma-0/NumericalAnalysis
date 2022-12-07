import matplotlib.pyplot as plt
import numpy as np


from _Data import getDataSet
from _FillMatrix import fill_matrix_A, fill_matrix_y
from _FindCoefficent import Thomas_Algorithm, find_coeff_B, find_coeff_D


def main():
    nodes = getDataSet('./data/point_task.txt')
    # nodes = getDataSet('./data/additional point.txt')
    x_ = [i.x for i in nodes]
    y_ = [i.f for i in nodes]

    h = round((nodes[-1].x-nodes[0].x)/len(nodes), 1)  # step

    A = fill_matrix_A(n=int(len(nodes)), h=h)
    y = fill_matrix_y(nodes=nodes, h=h)

    coeff_C = Thomas_Algorithm(matrixA=A, matrixY=y, n=len(nodes))
    coeff_D = find_coeff_D(coeffC=coeff_C, h=h, n=len(nodes))
    coeff_B = find_coeff_B(nodes=nodes, coeffC=coeff_C,
                           coeffD=coeff_D, h=h, n=len(nodes))

    ###
    # Draw splines
    ###

    dx = x_[0]
    h_spline = h/10

    x_spline = []
    y_spline = []

    for i in range(len(nodes)):
        while dx <= x_[i]:
            x_spline.append(dx)
            y_spline.append(nodes[i].f + coeff_B[i]*(dx-x_[i]) +
                            coeff_C[i]/2 * (dx-x_[i])**2 + coeff_D[i]/6 * (dx-x_[i])**3)
            dx += h_spline

    print(len(x_spline))

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_title('Source')
    ax1.plot(x_, y_, color='green')
    ax1.scatter(x_, y_, color='black')

    ax2.set_title('Interpolated')
    ax2.plot(x_spline, y_spline, color='red')
    ax2.scatter(x_spline, y_spline, color='gray', linewidths=0.25)

    plt.show()


if __name__ == '__main__':
    main()
