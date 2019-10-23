"""
定义和使用学生类
Version: 0.1
Author: 骆昊
Date: 2019-10-23
"""

def _foo():
	print('test')

class Student(object):
	def __init__(self,name,age):
		self.name = name 
		self.age = age

	def study(self,course_name):
		print('%s正在学习%s' % (self.name,course_name))
	def watch_ac(self):
		if self.age < 18:
		   print('%s只能看熊出没。' % self.name)
		else:
		   print('%s正在观看大电影.' % self.name)

def main():
	stu1 = Student('lsl',25)
	stu1.study('Python')
	stu1.watch_ac()
	stu2 = Student('sa',14)
	stu2.study('sxpd')
	stu2.watch_ac()

if __name__ == '__main__':
	main()