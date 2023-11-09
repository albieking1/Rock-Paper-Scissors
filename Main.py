import random
user_move = input("Scissors, Paper, rock: ")
possible_move = ["Scissors", "Paper", "Rock"]
ai_move = random.choice(possible_move)
print(f"\nYour move {user_move}, ai's move {ai_move}.\n")
if user_move == ai_move:
 print(f"Both players selected {user_move}. Tie!")
