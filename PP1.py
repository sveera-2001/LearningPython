list_1 = list(map(int,input("Enter the elements:").split(" ")))
num = int(input("Enter a number:"))
list_2 = []
count = 0
for ele in list_1:
	if ele < num:
		list_2.append(ele)
		count+=1
if count > 0:	
    print(list_2)
else:
		print("List empty")
