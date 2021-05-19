"""
输入月收入和五险一金计算个人所得税
应纳所得额=税前工资收入金额-五险一金(个人缴纳部分)-起征点(5000元)=12000-1100-5000=5900元
Date: 2019-10-9
"""

salary = float(input('请输入本月收入:'))
insurance = float(input('五险一金:'))
diff = salary - insurance - 5000
if diff <= 0:
	rate = 0
	deduction = 0
elif diff < 3000:
    rate = 0.03
    deduction = 0
elif diff < 12000:
    rate = 0.1
    deduction = 210
elif diff < 25000:
    rate = 0.2
    deduction =1410
elif diff < 35000:
    rate = 0.25
    deduction = 2660
elif diff < 55000:
    rate = 0.3
    deduction = 4410
elif diff < 80000:
    rate = 0.35
    deduction = 7160
else:
    rate = 0.45
    deduction = 15160
tax = abs(diff * rate -deduction)
print('个人所得税:￥%.2f元' % tax)
print('实际到手收入: ￥%.2f元' % (diff + 5000 - tax))
