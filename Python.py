#making rock paper scissors game

#random number 1-3, 1 is rock, 2 is paper, 3 is scissors
import random 
def play():
    #don't have to define variables in python, just assign them
    user = input("Enter your choice (rock, paper, scissors):")
    computer = random.randint(1,3)
    if computer == 1:
        computer_choice = "rock"
    elif computer == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"
    print("Computer chose:", computer_choice)
    if user == computer_choice:
        print("It's a tie!")
    elif user == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif user == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif user == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")
        play()