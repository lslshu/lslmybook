'''
百分制成绩转等级制成绩
90分以上，输出A
80分~89分，输出B
70分~79分，输出C
60分~69分，输出D
60分以下，输出E

data:2019-10-9
'''

score = float(input('请输入成绩:'))
if score >= 90:
	grade = 'A'
elif score >= 80:
	grade = 'B'
elif score >=70:
	grade = 'C'
elif score >=60:
	grade = 'D'
else:
	grade = 'E'
print('对应成绩为:', grade)