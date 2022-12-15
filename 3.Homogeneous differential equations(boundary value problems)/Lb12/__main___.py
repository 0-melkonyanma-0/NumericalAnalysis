import matplotlib.pyplot as plt
import numpy as np


def getX(h) -> list:
    list_x = []
    i = 0
    while i <= 1+h:
        list_x.append(i)
        i += h
    return list_x


n = 1000
h = 1/n
y_start = 1
y_end = 1/3

list_x = getX(h)

matrix = np.zeros((n, n))
y = np.zeros((n))

for i in range(1, n-1):
    matrix[i][i] = -2
    matrix[i-1][i] = 1
    matrix[i][i-1] = 1
matrix[0][0] = 1
matrix[0][1] = 0
matrix[n-2][n-1] = 1
matrix[n-1][n-1] = 1/3

for i in range(1, n-1):
    y[i] = list_x[i]*h**2


y[0] = y_start
y[n-1] = y_end

a = np.linalg.solve(matrix, y)

plt.plot(list_x[0:-1], a)
plt.grid()
plt.legend(['Метод прогонки'])
plt.show()
