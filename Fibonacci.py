num = int(input("Enter the last number:"))
first = 0
second = 1
print("Fibonacci series:")
print(first) #FibonacciSeries
print(second)
for i in range(1,num):
	third = first+second
	first = second
	second = third
	if third<=8:
		print(third)
