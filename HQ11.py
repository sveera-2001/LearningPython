N = int(input())
Rec = []
for i in range(N):
	Name = input()
	marks = float(input())
	Rec.append(list([marks,Name]))
Rec.remove(max(Rec))
temp = max(Rec)
for i in Rec:
	if i[0] == temp[0]:
		if i[1] > temp[1]:
			print(temp[1])
			print(i[1])
		else:
			print(i[1])
			print(temp[1])
		 
