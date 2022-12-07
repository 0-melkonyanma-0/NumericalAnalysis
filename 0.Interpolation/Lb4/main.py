from Least_Square_Method import Least_Square
from _Data import getDataSet
import matplotlib.pyplot as plt
import numpy as np
import os


def main():
    nodes = getDataSet('./data/point.txt')
    x_plt = [i.x for i in nodes]
    y_plt = [i.f for i in nodes]
    os.system('clear')
    coord = Least_Square(x_plt, y_plt)
    print(coord)
    x = np.linspace(nodes[0].x, nodes[-1].x)
    y = x*coord[0] + coord[-1]
    plt.plot(x, y, color='red')
    plt.scatter(x_plt, y_plt, linewidths=1, color='green')
    plt.show()


if __name__ == '__main__':
    main()
