import random
choices = ["rock", "paper", "scissors"]
bot = random.choice(choices)
player = input("choose rock, paper, or scissors:")
if bot == player:
    print("It's a tie")
elif (player == "rock" and bot == "scissors") or (player == "paper" and bot == "rock") or (player == "scissors" and bot == "paper"):
    print("You win")
else:
    print("You lose")