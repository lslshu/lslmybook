"""
多个线程共享数据 - 有锁的情况

Date: 2019-11-14
"""

import time
import threading

class Account(object):

	def __init__(self):
		self._balance = 0
		self._lock = threading.Lock()


	def deposit(self,money):
		self._lock.acquire()
		try:
			new_balance = self._balance + money
			time.sleep(0.01)
			self._balabce = new_balance
		finally:
			self._lock.release()

	@property
	def balance(self):
		return self._balance

if __name__ == '__main__':
	account = Account()
	for _ in range(100):
		threading.Thread(target=account.deposit,args=(1,)).start()
	time.sleep(2)
	print('账户余额为: ￥%d元' % account.balance)