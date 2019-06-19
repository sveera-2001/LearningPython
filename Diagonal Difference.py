def diagonal_difference(matrix, size):
	primary_diagonal, secondary_diagonal = list(), list()
	for index in range(size):
		primary_diagonal.append(matrix[index][index])
		secondary_diagonal.append(matrix[index][(size - 1) - index])
	result = sum(primary_diagonal) - sum(secondary_diagonal)
	return abs(result)

size = int(input())
matrix = list()
for i in range(size):
	line = list(map(int, input().split()))
	matrix.append(line)
print(diagonal_difference(matrix, size))
