num = int(input("Enter a number:"))
count = 0
for i in range(1,num+1):
	if num%i==0:
		count+=1
if count==2: #Primenumber
	print(num,"is Prime Number")
else:
	print("Not a prime number")
