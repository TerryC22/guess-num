import random

r = random.randint(1,100)
i = 0
while True:
	i = i + 1
	x = input('1~100請猜一個數字：')
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
