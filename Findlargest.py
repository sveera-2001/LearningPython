print("Enter three numbers:")
n1 = int(input())
n2 = int(input())
n3 = int(input())  #Findlargest
if n1>n2 and n1>n3:
	print(n1,"is the largest")
elif n2>n1 and n2>n3:
	print(n2,"is the largest")
else:
	print(n3,"is the largest")
