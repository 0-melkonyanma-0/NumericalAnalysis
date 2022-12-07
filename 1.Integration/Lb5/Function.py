import math


# f1 sin(1/x^2) x in [3,5]
#
# f2 ln(x)*sin(1/x^3) x in [3,4]
#
# f3 (e^2x)*cos(1/x) x in [1,2]
#
# f4 ((e^x)/x)*sin(1/x^3) x in [2,3]
#
# f5 ((3^x)/x^2)*ln(x^2) x in [1,2]


def f1(x): return math.sin(1/x**2)
def f1_interval(): return [3, 5]


def f2(x): return math.log(x)*math.sin(1/x**3)
def f2_interval(): return [3, 4]


def f3(x): return math.e**(2*x)*math.cos(1/x)
def f3_interval(): return [1, 2]


def f4(x): return (math.e**x/x)*math.sin(1/x**3)
def f4_interval(): return [2, 3]


def f5(x): return (3**x/x**2)*math.log(x**2)
def f5_interval(): return [1, 2]
