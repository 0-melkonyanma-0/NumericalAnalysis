from AitkenScheme import AitkenScheme
from Lagrange import Lagrange
from _DrawGraph import Draw_Graph
from _Data import getDataSet
from os import system
import platform
from time import time

if platform.system() == 'Windows':
    system('cls')
else:
    system('clear')


# './data/Interpolation/1000pointslb1.txt'
# "./data/Interpolation/points_tasklb1_.txt"

_path_ = "./data/Interpolation/points_tasklb1.txt"
nodes = getDataSet(_path_)
