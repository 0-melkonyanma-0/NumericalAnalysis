from math import factorial


def first_gauss(nodes, diff_table, int_point) -> float:
    result = diff_table[0]
    t_i = 1
    numert = 1
    h = nodes[1].x - nodes[0].x
    t = (int_point - nodes[int(len(nodes)/2)].x)/h

    for i in range(1, len(diff_table)):
        if i % 2 == 0:
            numert *= t-t_i
            t_i += 1
        else:
            numert *= t+i-t_i

        result += (numert*diff_table[i])/factorial(i)

    return result


def second_gauss(nodes, diff_table, int_point) -> float:
    result = diff_table[0]
    t_i = 1
    numert = 1
    h = nodes[1].x - nodes[0].x
    t = (int_point - nodes[int(len(nodes)/2)].x)/h

    for i in range(1, len(diff_table)):
        if i % 2 == 0:
            numert *= t+t_i
            t_i += 1
        else:
            numert *= t-i+t_i

        result += (numert*diff_table[i])/factorial(i)

    return result
