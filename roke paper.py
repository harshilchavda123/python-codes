import random

# Define the possible choices
choices = ["rock", "paper", "scissors"]

# Get the player's choice
player_choice = input("Choose your weapon: rock, paper, or scissors? ")

# Get the computer's choice
computer_choice = random.choice(choices)

# Display the choices
print("You chose:", player_choice)
print("The computer chose:", computer_choice)

# Determine the winner
if player_choice == computer_choice:
    print("Tie!")
elif player_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("You lose!")
elif player_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")