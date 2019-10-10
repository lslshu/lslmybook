"""
用while循环实现1~100之间的偶数求和
Date: 2019-10-10
"""

sum = 0
num = 0
while num<=100:
	sum += num
	num += 2
print(sum)