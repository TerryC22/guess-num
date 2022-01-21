import random

r = random.randint(1,100)
i = 0
while True:
	i = i + 1
	x = input('1~100請猜一個數字：')
	x_int = int(x)
	if x_int == r:
		if i == 1:
			print('猜對了')
			break
		else:
			print('終於猜對了')
			break
	elif x_int > r:
		print('比答案大')
	else:
		print('比答案小')
