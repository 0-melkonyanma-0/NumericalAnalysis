import numpy as np


def AitkenScheme(nodes: list, inter_point: float, eps: float) -> float:
    nodes_ = np.copy(nodes)
    div_dif = list()
    offset = 1
    indx = 0
    eps_min = np.array([], float)
    flag = 0
    # abs(xi-x)
    #
    dif_xi = list()

    for i in range(len(nodes_)):
        dif_xi.append(abs(inter_point-nodes_[i].x))

    for i in range(len(nodes_)-1):
        for j in range(len(nodes_)-i-1):
            if dif_xi[j] > dif_xi[j+1]:
                nodes_[j], nodes_[j+1] = nodes_[j+1], nodes_[j]
                dif_xi[j], dif_xi[j+1] = dif_xi[j+1], dif_xi[j]

    tabel_div_dif = [[i.f for i in nodes_]]

    for i in range(len(nodes_)-1):
        for j in range(len(tabel_div_dif[i])-1):
            fract_part = 1/(nodes_[j+offset].x-nodes_[j].x)
            div_dif.append(fract_part*(tabel_div_dif[i][j+1]*(inter_point - nodes_[j].x) -
                                       tabel_div_dif[i][j]*(inter_point - nodes_[j+offset].x)))
        tabel_div_dif.append(div_dif)
        div_dif = []
        offset += 1

        eps_min = np.append(
            eps_min, [abs(tabel_div_dif[i+1][0] - tabel_div_dif[i][0])])

        if eps_min[i] < eps:
            flag = 1
            indx = i
            break

    print("Number of iterations : ", indx+1)
    
    if flag == 0:
        return tabel_div_dif[np.argmin(eps_min)][0]
    else:
        return tabel_div_dif[indx][0]
