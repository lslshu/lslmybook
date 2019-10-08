'''
输入年份 如果是闰年输出True 否则输出False
Data:2019-9-29
'''
year = int(input('请输入年份： '))
is_leap = (year % 4 == 0 and year % 4 != 0 or year % 400 == 0 )
print(is_leap)