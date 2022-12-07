import _PointClass
import math

startPoint = 1
endPoint = 2
test = list()


while startPoint < endPoint:
    test.append(_PointClass.Point(float('{:,.4f}'.format(startPoint)), float(
        '{:,.4f}'.format(math.e**startPoint))))
    startPoint += 0.001


with open('./data/Interpolation/1000pointslb1.txt', 'w', encoding='utf-8') as f:
    for i in range(len(test)):
        f.write(f'{test[i].x} {test[i].f}\n')
