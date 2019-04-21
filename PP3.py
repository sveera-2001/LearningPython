a = list(map(int,input("Enter elements:").split(" ")))
b = list(map(int,input("Enter elements:").split(" ")))
c = []
count = 0
for ele_1 in a:
	for ele_2 in b:
	    if ele_1==ele_2: 
		    c.append(ele_1)
		    count+=1
if count==0:
	print("No common elements")
else:
	print(c)
