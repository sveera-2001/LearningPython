def maximize(A,B,C,D,Z):
	values = []
	for alpha in [A,B,C,D]:
		value = (int(Z[0]) * int(alpha[0])) + (int(Z[2]) * int(alpha[2]))
		values.append(value) 
	return values
	
A,B,C,D = ([] for i in range(4))
for alpha in [A,B,C,D]:
	ele = input()
	alpha.append(ele.split(",")

Z = input()
print(maximize(A,B,C,D,Z))



 



