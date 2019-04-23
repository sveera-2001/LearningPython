def removedupe1(lis):
	return set(lis)
def removedupe2(lis):
	lis_t = []
	for ele in lis:
		if ele not in lis_t:
			lis_t.append(ele)
	return lis_t
lis = list(map(int,input().split()))
print(removedupe1(lis))
print(removedupe2(lis))
