def plus_minus(array):
	count_p, count_n, count_z = 0, 0, 0
	for ele in array:
		if ele > 0:
			count_p += 1
		elif ele < 0:
			count_n += 1
		else:
			count_z += 1
	
	print(count_p / len(array))
	print(count_n / len(array))
	print(count_z / len(array))


size = int(input())
array = [int(x) for x in input().split()]
plus_minus(array)
