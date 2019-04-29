lb = 0
ub = 100
count = 0
while lb<=ub:
	count += 1
	guess = (lb+ub)//2
	print(guess)
	user_num = int(input("Enter a num:"))
	if user_num == 1:
		lb = guess + 1
	elif user_num == 2:
		ub = guess - 1
	elif user_num == 0:
		break
print("Number of loops:",count)
