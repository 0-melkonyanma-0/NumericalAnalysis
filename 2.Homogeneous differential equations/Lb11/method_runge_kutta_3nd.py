def method_runge_kutta(list_x, h, amount_el):
    list_y = [1]
    for i in range(1, amount_el):
        k1 = func(list_x[i], list_y[i-1])
        k2 = func(list_x[i]+h/3, list_y[i-1]+h*k1*2/3)
        k3 = func(list_x[i]+h*2/3, list_y[i-1]+h*k2*2/3)
        list_y.append(list_y[i-1]+1/4*h*(k1+3*k3))

    return list_y


def func(x, y):
    return y + x**2
