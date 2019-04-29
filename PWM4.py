def showNumbers(limit):
	for num in range(limit+1):
		if num %2 == 0:
			parity = "EVEN"
		else:
			parity = "ODD"
		print(num,parity)

limit = int(input("Enter the limit:"))
showNumbers(limit)
