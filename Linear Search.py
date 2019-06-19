def linearsearch(lis, item):
	counter = 0
	for element in item:
		counter += 1
		if element == item:
			return counter
		else:
			continue
print(linearsearch(["Apple", "Orange", "Banana", "Dogs", "Icecream"], "Apple"))
