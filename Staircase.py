def staircase(size):
	for i in range(size):
		print(" " * (size - 1 - i), end="")
		print("#" * (i + 1))
size = int(input())
staircase(size)
