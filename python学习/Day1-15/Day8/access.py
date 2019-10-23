class Test:
	"""docstring for Test"""
	def __init__(self, foo):
		super(Test, self).__init__()
		self.__foo = foo

	def __bar(self):
		print(self.__foo)
		print('__bar')

def main():
	test = Test('hello')
	test._Test__bar()
	print(test._Test__foo)


if __name__ == '__main__':
	main()