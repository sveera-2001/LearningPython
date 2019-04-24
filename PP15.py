def reverse_string(string):
	result = string.split()
	for i in range(1,len(result)+1):
		print(result[-i],end=" ")
		
string = input("Enter a string:")
reverse_string(string)
