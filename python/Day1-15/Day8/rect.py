"""
定义和使用矩形类

Date: 2019-10-23
"""

class Rect(object):
	'''矩形类'''

	def __init__(self,width=0,height=0):
		'''初始化方法'''
		self._width = width
		self._height = height


	def perimeter(self):
		'''计算周长'''
		return (self._width + self._height) * 2

	def area(self):
		'''计算面积'''
		return self._width * self._height

	def _str_():
		'''矩形对象的字符串表达式'''
		return '矩形[%f,%f]' % (self._width,self._height)

	def _del_(self):
		'''析构器'''
		print('销毁矩形对象')


if __name__ == '__main__':
	rect1 = Rect()
	print(rect1)
	print(rect1.perimeter())
	print(rect1.area())
	rect2 = Rect(3.5,4.5)
	print(rect2)
	print(rect2.perimeter())
	print(rect2.area())