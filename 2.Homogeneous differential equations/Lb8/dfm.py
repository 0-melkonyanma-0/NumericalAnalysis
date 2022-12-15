def dfm_method(list_x, h):
    list_y = [1, 1]

    for i in range(2, len(list_x)):
        # list_y.append(((4*h**2)+2)*list_y[i]-list_y[i-1])
        list_y.append(list_x[i]**2*h**2+2*list_y[i-1]-list_y[i-2])
    # (list_x[i-1]**2)*(h**2)+2*list_y[i-1]-list_y[i-2]
    return list_y
