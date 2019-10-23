"""
另一种创建类的方式

Date: 2019-10-22
"""

def bar(self,name):
	self._name = name

def foo(self,course_name):
	print('%s正在学习%s.' % (self._name,course_name))

def main():
	Student = type('Student',(object,),dict(__init__=bar,study=foo))
	stu1 = Student('lsl')
	stu1.study('Python study')

if __name__ == '__main__':
	main()