import random
RPSchoices = ["rock", "paper", "scissors"]
a = True

while a == True:
    CPUchoice = random.choice(RPSchoices)
    playerChoice = input("Rock, Paper, or Scissors?: ")
    playerChoice = (playerChoice.lower())

    if playerChoice == CPUchoice:
        print("Both players slected " + playerChoice + ", it's a tie!")
    elif playerChoice == "rock":
        if CPUchoice == "scissors":
            print("CPU chose " + CPUchoice + ", you win!")
        else:
            print("CPU chose " + CPUchoice + ", you lose!")
    elif playerChoice == "paper":
        if CPUchoice == "rock":
            print("CPU chose " + CPUchoice + ", you win!")
        else:
            print("CPU chose " + CPUchoice + ", you lose!")
    elif playerChoice == "scissors":
        if CPUchoice == "paper":
            print("CPU chose " + CPUchoice + ", you win!")
        else:
            print("CPU chose " + CPUchoice + ", you lose!")
