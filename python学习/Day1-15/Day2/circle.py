'''
输入半径计算圆的周长和面积
圆周长字母公式为：C=πD=2πR
圆的面积:S=πr²=πd²/4
Data：2019-9-29
'''

import math

radius = float(input('请输入圆的半径： '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长： %.2f' % perimeter)
print('面积： %.2f' % area)