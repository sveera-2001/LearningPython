num = int(input("Enter a number:"))
num2 = num
num1 = 0   #ArmstrongNumber
ndig = len(str(num))
while num>0:
	digit = num%10
	num1 += (digit**ndig)
	num //= 10
if num1==num2:
	print("Armstrong Number")
else:
	print("Not An Armstrong Number")
