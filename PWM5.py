def sum_multiple(limit):
	summ = 0
	for num in range(limit+1):
		if num %3 == 0 or num %5 == 0:
			summ += num
	return summ

limit = int(input("Enter a number:"))
print(sum_multiple(limit))
