# import the random function
import random

from random

# create statement for the user
player = input("Enter a choice (rock, paper, scissors): ")
# create statement for the player choices
selections = ["rock", "paper", "scissors"]
# create statement for the 
opponent = random.choice(selections)
print(f"You chose {player}, computer chose {opponent}. ")

if player == opponent:
    print(f"Both players selected {player}. It's a tie!")
elif player == "rock":
    if opponent == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif player == "paper":
    if opponent == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif player == "scissors":
    if opponent == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")