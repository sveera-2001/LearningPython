def isprime(num):
	div_count = 0
	for div in range(1,num+1):
		if num%div == 0:
			div_count+=1
	if div_count == 2:
		print(num, "is a prime number")
	else:
		print(num, "is not a prime number")

num = int(input("Enter a number:"))
isprime(num)
