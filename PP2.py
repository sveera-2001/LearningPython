num = int(input("Enter number:"))
if_prime = 0
divisors = []
for div in range(1,num+1):
	if num%div==0:
		divisors.append(div)
		if_prime+=1
print("Divisors:",divisors)
if if_prime==2:
	print("Also, it's a prime number")
else:
	print("Nope, not a prime")
