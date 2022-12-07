import matplotlib.pyplot as plt
import numpy as np


def Draw_Graph(inter_point: float, f_i: float, nodes: list) -> None:
    x = np.array([], float)
    y = np.array([], float)
    for i in nodes:
        x = np.append(x, [i.x])
        y = np.append(y, [i.f])

    plt.scatter(inter_point, f_i, color='r', linewidths=1)
    plt.plot(x, y, linestyle='--', color='g', linewidth=2)
    plt.title('Function e^x\n', fontdict={
              'fontname': 'Arial', 'fontsize': '15'})
    plt.xlabel('X Axis', fontdict={'fontname': 'Arial'})
    plt.ylabel('Y Axis', fontdict={'fontname': 'Arial'})
    plt.show()
