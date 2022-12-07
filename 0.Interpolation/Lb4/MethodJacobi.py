import numpy as np
import math


def Jacobi(matrics_A: np.array, matrics_B: np.array, n: int):
    eps = 1e-6
    norm = 1000
    LU = np.zeros((n, n))
    D = np.zeros((n))
    x = np.zeros((n))
    xk = np.zeros((n))

    for i in range(n):
        for j in range(n):
            if i != j:
                LU[i][j] = matrics_A[i][j]
                continue
        D[i] = matrics_A[i][i]

    for i in range(n):  # first
        x[i] = 1 + matrics_B[i]/D[i]

    while math.sqrt(norm) >= eps:
        for i in range(n):
            xk[i] = x[i]

            summ = 0.0

            for j in range(n):
                summ += LU[i][j]*xk[j]

            x[i] = (1/D[i])*(matrics_B[i]-summ)

            if i == 0:
                norm = math.fabs(xk[i]-x[i])

            if math.fabs(xk[i]-x[i]) > norm:
                norm = math.fabs(xk[i]-x[i])

    return x
