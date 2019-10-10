"""
输入非负整数n计算n!
Date: 2019-10-10
"""

n = int(input('n = '))
result = 1
for x in range(1,n+1):
	result *= x
print('%d! = %d' %(n,result))