a = list(map(int,input("Enter the elements:").split()))
b = [i for i in a if i%2 == 0]
print("Result:",b)
