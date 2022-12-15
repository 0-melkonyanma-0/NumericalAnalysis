def method_runge_kutta(list_x: list, h: float):
    list_y = [1]
    list_z = [2]
    for i in range(1, len(list_x)):
        k1 = funcZ((list_z[i-1]))*h
        m1 = funcY((list_y[i-1]))*h
        k2 = funcZ((list_z[i-1]+m1/2))*h
        m2 = funcY((list_y[i-1]+k1/2))*h
        k3 = funcZ((list_z[i-1]+2*m2-m1))*h
        m3 = funcY((list_y[i-1]+2*k2-k1))*h
        list_y.append(list_y[i-1]+1/6*(k1+4*k2 + k3))
        list_z.append(list_z[i-1]+1/6*(m1+4*m2 + m3))
    return list_y


def funcZ(z: float):
    return z


def funcY(y: float):
    return 4*y
