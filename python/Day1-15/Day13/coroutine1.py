"""
使用协程 - 模拟快递中心派发快递

Date: 2019-11-14
"""

from time import sleep
from random import random

def build_deliver_man(man_id):
	total = 0
	while True:
		total += 1
		print('%d号快递员准备接今天的第%d单.' % (man_id, total))
		pkg = yield
		print('%d号快递员收到编号为%s的包裹.' % (man_id, pkg))
		sleep(random() * 3)

def package_center(deliver_man,max_per_day):
	num = 1
	deliver_man.send(None)
	#next(deliver_man)
	while num <= max_per_day:
		package_id = 'PKG-%d' % num
		deliver_man.send(package_id)
		num += 1
		sleep(0.1)
	deliver_man.close()
	print('今天的包裹派送完毕！')

dm = build_deliver_man(1)
package_center(dm,10)