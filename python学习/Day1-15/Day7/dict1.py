"""
定义和使用字典
Date: 2019-10-17
"""

def main():
	scores = {'qaz':95,'wsx':78,'edc':82}
	print(scores['qaz'])
	print(scores['wsx'])
	for elem in scores:
		print('%s\t--->\t%d' % (elem, scores[elem]))
	scores['wsx'] = 65
	scores['rfv'] = 71
	scores.update(qw=67,asd=85)
	print(scores)
	if 'zxc' in scores:
		print(scores['zxc'])
	print(scores.get('zxc'))
	print(scores.get('zxc',60))
	print(scores.popitem())
	print(scores.popitem())
	print(scores.pop('qaz',100))
	scores.clear()
	print(scores)


if __name__ == '__main__':
	main()
