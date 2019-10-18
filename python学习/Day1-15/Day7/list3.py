"""
生成列表
- 用range创建数字列表
- 生成表达式
- 生成器

Date: 2019-10-17
"""

def fib(n):
	a,b = 0,1
	for _ in range(n):
		a,b = b,a+b
		yield a

def main():
	list1 = list(range(1,11))
	print(list)
	list2 = [x*x for x in range(1,11)]
	print(list2)
	list3 = [m+n for m in 'ABCDEFG' for n in '12345']
	print(list3)
	print(len(list3))
	gen = (m+n for m in 'ABCDEFG' for n in '12345')
	print(gen)
	for elem in gen:
		print(elem,end=' ')
	print()
	gen = fib(20)
	print(gen)
	for elem in gen:
		print(elem,end=' ')
	print()


if __name__ == '__main__':
	main()