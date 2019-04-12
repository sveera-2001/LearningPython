year = int(input("Enter the year:"))
if year%4==0 and year%100!=0:
	print("Leap year")
elif year%400==0:  #leapyear
	print("Leap year")
else:
	print("Not a leap year")
	
	
