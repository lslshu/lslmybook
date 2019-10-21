"""
双色球随机选号程序

Date: 2019-10-18
"""

from random import randrange,randint,sample

def display(balls):
	'''
    输出列表中的双色球号码
	'''
	for index,ball in enumerate(balls):
		if index == len(balls) -1:
			print('|',end=' ')
		print('%02d' % ball, end=' ')
	print()


def random_select():
	'''
    随机选择一组号码
	'''
	red_balls = [x for x in range(1,34)]
	selected_balls = []
	for _ in range(6):
		index = randrange(len(red_balls))
		selected_balls.append(red_balls[index])
		del red_balls[index]
	selected_balls.sort()
	selected_balls.append(randint(1,16))
	return selected_balls

def main():
	n = int(input('机选几注： '))
	for _ in range(n):
		display(random_select())

if __name__ == '__main__':
	main()