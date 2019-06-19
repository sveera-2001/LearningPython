def mini_max_sum(array):
	for index in range(len(array)):
		for index1 in range(index + 1, len(array)):
			if array[index] > array[index1]:
				temp = array[index]
				array[index] = array[index1]
				array[index1] = temp
	sum1 = sum(array[:len(array) - 1])
	sum2 = sum(array[1:len(array)])
	print(sum1, sum2)
array = list(map(int, input().split()))
mini_max_sum(array)
