import numpy as np
from MatrixOperation import *
from MethodJacobi import Jacobi


def Least_Square(x: list, y: list):
    n = len(x)
    m = 2
    Ax = np.zeros((n, m))
    b = np.zeros((n))

    for i in range(n):
        Ax[i][0] = x[i]
        Ax[i][1] = 1.0
        b[i] = y[i]

    AxT = Transposition(m, n, Ax)
    # print(Ax)
    # print(AxT)
    Ax_ = MatricsMultMatrics(AxT, Ax, m, n, n, m)
    print(Ax_)
    b_ = MatricsMultMatrics(AxT, b, m, n, n, 1)
    print(b_)
    x_ = Jacobi(Ax_, b_, m)

    return x_
