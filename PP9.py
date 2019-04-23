import random
random = random.randint(1,9)
guess = int(input("Enter a number:"))
if random == guess:
	print("Your guess is right!")
elif random > guess:
	print("Your guess is too low")
elif random < guess:
	print("Your guess is too high")
