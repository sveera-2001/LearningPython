def binary_search(array,num):
	Lb = 0
	Ub = len(array)-1
	while Lb <=Ub:
		mid = (Lb+Ub)//2
		if array[mid] == num:
			print(num," is at ",mid)
			break
		elif array[mid] > num:
			Ub = mid - 1
		elif array[mid] < num:
			Lb = mid + 1

array = list(map(int,input("Enter the elements:").split()))
num = int(input("Enter the number:"))
binary_search(array,num)
