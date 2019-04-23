import random
A = random.sample(range(100),5)
B = random.sample(range(100),7)
result = [num for num in set(A) if num in B]
print(result)
