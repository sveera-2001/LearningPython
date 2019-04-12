num = int(input("Enter a number:"))
num1 = num
ndig = len(str(num))-1
num2 = 0  #palindrome
while num>0 :
	digit = num%10
	num2 += (digit*(10**ndig))
	ndig -=1
	num //=10
if num1==num2:
	print("Palindrome")
else:
	print("Not a palindrome")
	   
