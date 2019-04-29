def find_max(a,b,c):
	if a > b and a > c:
		print(a,"is the largest")
	elif b > a and b > c:
		print(b,"is the largest")
	else:
		print(c,"is the largest")

a,b,c = [int(input()) for i in range(3)]
find_max(a,b,c)
