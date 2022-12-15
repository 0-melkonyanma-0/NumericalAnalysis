import matplotlib.pyplot as plt
import math
from runge import rung_3rd

a = 0
b = 2
y0 = 0
y1 = math.pi

h = 0.1

alpha0 = math.atan((y1-y0)/(b-a))
z0 = math.tan(y1-y0)/(b-a)
eps = 1e-4

x = []
y = []
x.append(a)
y.append(y0)

rung_3rd(z0, x, y, h, b)

check0 = y[-1] - y1

if (math.fabs(y[-1]-y1) < eps):
    plt.legend(['Метод стрельбы'])
    plt.grid()
    plt.plot(x, y)
    plt.show()

else:

    alpha1 = alpha0

    if y[-1] > y1:  # y(b,alpha0) < b
        while y[-1] > y1:

            alpha1 /= 1.5
            z0 = math.atan(alpha1)
            x.clear()
            x.append(a)
            y.clear()
            y.append(y0)
            rung_3rd(z0, x, y, h, b)
    else:   # if y(b,alpha0) > b

        while y[-1] < y1:
            alpha1 *= 1.5
            z0 = math.tan(alpha1)
            x.clear()
            x.append(a)
            y.clear()
            y.append(y0)
            rung_3rd(z0, x, y, h, b)

        # метод половниного деления для поиска
        # _alpha в интервале (alpha0,alpha1)

        while math.fabs(y[-1]-y1) > eps:
            alpha2 = (alpha0 + alpha1) / 2
            check1 = y[-1] - y1
            z0 = math.tan(alpha2)
            x.clear()
            x.append(a)
            y.clear()
            y.append(y0)
            rung_3rd(z0, x, y, h, b)
            check2 = y[-1] - y1

            if check0 * check2 < 0:
                alpha1 = alpha2
            else:
                alpha0 = alpha1
                alpha1 = alpha2
                check0 = check1

        _alpha = (alpha0 + alpha1) / 2.0
        z0 = math.tan(_alpha)
        x.clear()
        x.append(a)
        y.clear()
        y.append(y0)
        rung_3rd(z0, x, y, h, b)

plt.grid()
plt.plot(x, y)
plt.legend(['Метод стрельбы'])
plt.show()
