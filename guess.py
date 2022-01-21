while True:
	upper = input('請輸入猜的範圍上限：')
	upper_int = int(upper)
	lower = input('請輸入猜的範圍下限：')
	lower_int = int(lower)
	if lower_int >= upper_int:
		print('下限要比上限小')
	else:
		break

import random
r = random.randint(lower_int,upper_int)
i = 0
while True:
	i = i + 1
	x = input('請猜一個數字：')
	x_int = int(x)
	if x_int == r:
		if i == 1:
			print('你1次就猜對了！好棒棒！')
			break
		else:
			print('你猜', i, '次終於猜對了！還不賴！')
			break
	elif x_int > r:
		print('比答案大')
	else:
		print('比答案小')
	print('這是你猜的第', i, '次')
