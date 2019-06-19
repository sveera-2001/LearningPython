def birthday_cake(array):
	count = 0
	large = array[0]
	for ele in array:
		if ele > large:
			large = ele
	for ele in array:
		if ele == large:
			count += 1
	return count
size = int(input())
array = list(map(int, input().split()))
print(birthday_cake(array))
