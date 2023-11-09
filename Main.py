import random
while True:
 user_move = input("Scissors, Paper, Rock: ")
 possible_move = ["Scissors", "Paper", "Rock"]
 ai_move = random.choice(possible_move)
 print(f"\nYour move {user_move}, ai's move {ai_move}.\n")
 if user_move == ai_move:
  print(f"Both players selected {user_move}. Tie!")
 elif user_move == "Rock":
  if ai_move == "Scissors":
   print("Rock smashes scissors, you win!")
  else:
   print("Paper covers rock, you lose!")
 elif user_move == "Paper":
  if ai_move == "Rock":
   print("Paper covers rock, you win!")
  else:
   print("Scissors cuts paper, you lose!")
 elif user_move == "Scissors":
  if ai_move == "Paper":
   print("Scissors cuts paper, you win!")
  else:
   print("Rock smashes scissors, you lose!")
 redo = input("Play again? (y/n): ")
 if redo.lower() != "y":
  break
