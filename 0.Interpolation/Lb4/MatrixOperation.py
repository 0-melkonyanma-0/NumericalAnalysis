import numpy as np


def Transposition(n: int, m: int, matrics: np.array):
    tr_matrics = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            tr_matrics[i][j] = matrics[j][i]

    return tr_matrics


def MatricsMultMatrics(first_matrics: np.array, second_matrics: np.array,
                       n1: int, m1: int, n2: int, m2: int):
    if m2 == 1:
        result = np.zeros((n1, m2))

        for i in range(n1):
            for j in range(n2):
                result[i] += first_matrics[i][j]*second_matrics[j]

        return result

    if m1 == n2:
        result = np.zeros((n1, m2))
        for i in range(n1):
            for j in range(m2):
                for k in range(n2):
                    result[i][j] += first_matrics[i][k]*second_matrics[k][j]

        return result
    else:
        print('Количество стоблцов первой матрицы\nне совпадают с количеством строк второй матрицы!')


def NumbMultMatrics(matrix: np.array, number: float, n: int, m: int):
    result = np.zeros((n, m))

    print(result)
    for i in range(n):
        for j in range(m):
            result[i][j] = matrix[i][j]*number

    return result
