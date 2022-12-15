import math

eps = 1e-4


def f(z):
    return z


def g(y):
    return -math.sin(y)


def rung_3rd(z0, x, y, h, b):

    while math.fabs(x[-1]-b) > eps:

        k1 = f(z0)*h
        m1 = g(y[-1])*h

        k2 = f(z0 + m1/2)*h
        m2 = g(y[-1] + k1/2)*h

        k3 = f(z0 + 2*m2 - m1)*h
        m3 = g(y[-1] + 2*k2 - k1)*h

        y.append(y[-1]+1/6*(k1 + 4*k2 + k3))
        z_1 = z0 + 1/6*(m1 + 4*m2 + m3)

        z0 = z_1

        x.append(x[-1]+h)
