import random

while True:
    # user's guess
    print("Make your guess; any # between 1 and 10")
    user_number = input()
    print("Your guess: " + user_number)

    # computer"s number
    computer_number = str(random.randint(1, 10))
    print("Computer's #: " + computer_number)

    # result
    if computer_number == user_number:
        print("Correct :)")
    else:
        print("Try again")
    print()



