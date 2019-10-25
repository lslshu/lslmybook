"""
属性的使用
- 访问器/修改器/删除器
- 使用__slots__对属性加以限制

Date: 2019-10-25
"""

"""
属性的使用
- 访问器/修改器/删除器
- 使用__slots__对属性加以限制

Date: 2019-10-25
"""

class Car(object):

	__slots__ = ('_brand','_max_speed')

	def __init__(self,brand,max_speed):
		self._brand = brand
		self._max_speed = max_speed

	@property
	def brand(self):
		return self._brand
	@brand.setter
	def brand(self,brand):
		self._brand = brand
	@brand.deleter
	def brand(self):
		del self._brand

	