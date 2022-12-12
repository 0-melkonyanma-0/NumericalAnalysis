# Order of approximation O(h)

def euler_method_explicit(list_x, step) -> list:
    list_y = [2.0]

    i = 0
    for i in range(1, len(list_x)):
        list_y.append(
            round((list_x[i-1]**2+3*list_y[i-1])/step+list_y[i-1], 3))

    return list_y

# Order of approximation O(h^2)


def euler_method_non_explicit(list_x, step) -> list:
    list_y = [2.0]
    h = 1/step

    for i in range(1, len(list_x)):
        list_y.append(
            round(
                ((list_y[i-1]*(1/h+3/2)+1/2*(list_x[i]**2+list_x[i-1]**2)))/(1/h-3/2), 3)
        )

    return list_y
