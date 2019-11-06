"""
写入CSV文件

Date: 2019-11-6
"""

import csv

class Teacher(object):

	def __init__(self,name,age,title):
		self._name = name
		self._age = age
		self._title = title
		self._index = -1

	@property
	def name(self):
		return self._name
	@property
	def age(self):
		return self._age
	