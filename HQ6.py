def func(y):
	if (y%4==0 and (y%100!=0 or y%400==0)):
		return True
	else:
		return False
y = int(input())
print(func(y))

		
