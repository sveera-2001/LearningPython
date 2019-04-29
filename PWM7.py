def print_prime(limit):
	count = 0
	for num in range(1,limit+1):
		for num1 in range(1,num+1):
			if num %num1 == 0:
				count+=1
		if count == 2:
			print(num,end=" ")
			count = 0
		else:
			count = 0

limit = int(input("Enter the limit:"))
print_prime(limit)
