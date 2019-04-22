p1_name = input("Player 1 name:")
p2_name = input("Player 2 name:")
start = input("Start game?")
while start == "yes":
	game_dict = {"rock": 1, "paper": 2,"scissor": 3}
	p1_choice = input("Player 1 turn:")
	p2_choice = input("Player 2 turn:")
	compare = game_dict.get(p1_choice) - game_dict.get(p2_choice)
	if compare == 0:
		print("Tie")
	elif compare in [-1,2]:
		print(p2_name, "wins!!!")
	elif compare in [1,-2]:
		print(p1_name, "winss!!!")
	start = input("Continue playing:")	
