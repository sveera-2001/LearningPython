def compare_triplets(a, b):
	count_a, count_b = 0, 0
	for i in range(3):
		if a[i] > b[i]:
			count_a += 1
		elif b[i] > a[i]:
			count_b += 1
	result = [x for x in [count_a, count_b]]
	return result

a = list(map(int, input().split()))	
b = list(map(int, input().split()))
result = compare_triplets(a, b)
for ans in result:
	print(ans, end=" ")
