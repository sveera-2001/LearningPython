X = int(input())
Y = int(input())
Z = int(input())
N = int(input())
temp = []
Lis = []
for i in range(X+1):
	for j in range(Y+1):
		for k in range(Z+1):
			if i+j+k !=N:
				temp = [i,j,k]
				Lis.append([i,j,k])
print(Lis)
