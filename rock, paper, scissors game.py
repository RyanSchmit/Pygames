import random
print("Make your choice: ")
choicey = input()
print("Your choice: " + choicey)

choices = ["rock", "paper", "scissors"]

computer_choice = random.choice(choices)
print("Computer's choice: " + computer_choice)


if choicey == computer_choice:
    print("It's a tie!")
if choicey == "rock" and computer_choice == "scissors":
	print("You win!")
if choicey == "rock" and computer_choice == "paper":
	print('You lose!')
if choicey == "paper" and computer_choice == "scissors":
	print('You lose!')
if choicey == "paper" and computer_choice == "rock":
	print("You win!")
if choicey == "scissors" and computer_choice == "paper":
	print('You win!')
if choicey == "scissors" and computer_choice == "rock":
	print("You lose!")


