import random


print("Welcome to ROCK, PAPER, SCISSORS\n")

def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        print("You win!\n")
    else:
        print("Computer wins!\n");

def construct():

    print("rock = 'r'")
    print("scissors = 's'")
    print("paper = 'p'")
    user = input("Entre your choice: ")
    if (user == 'r') or (user == 's') or (user == 'p'):
        computer = random.choice(['r', 'p', 's'])
        print("Computer's choice: ",computer)
        print("\n")
        if user == computer:
            print("It's a tie\n")
        else:
            win(user,computer)
    else:
        print("Please entre a valid character")


ch = 'y'
while ch=='y':
    construct()
    ch = input("Want to continue(y/n): ")
    print("\n")
