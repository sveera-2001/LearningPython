def gen_fibonacci(num):
	first, second = -1, 1
	for i in range(num):
		third = first + second
		print(third,end=" ")
		first, second = second, third
num = int(input("Enter the number:"))
gen_fibonacci(num)
