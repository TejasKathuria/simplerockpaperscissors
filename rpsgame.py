import random

options = ['rock', 'paper', 'scissors']

print("===Welcome to Rock Paper Scissors Game===")
userName = input("Enter your Name: ")
print(f"So {userName}, what do you want to choose?")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
print("4. Quit")
askUser = input("select the option [1/2/3/4]: ")
value = random.choice(options)
if askUser == "1":
    if value == "rock":
        print("it's a tie")
    elif value == "scissors":
        print(f"You Won! The robo picked up scissors. Congrats {userName}!")
    elif value == "paper":
        print("uh oh! You lost, it was a paper")
elif askUser == "2":
    if value == "paper":
        print("it's a tie")
    elif value == "stone":
        print(f"You Won! The robo picked up stone. Congrats {userName}!")
    elif value == "scissors":
        print("uh oh! You lost, it was a pair of scissors")
elif askUser == "3":
    if value == "scissors":
        print("it's a tie")
    elif value == "paper":
        print(f"You Won! The robo picked up paper. Congrats {userName}!")
    elif value == "stone":
        print("uh oh! You lost, it was a stone")