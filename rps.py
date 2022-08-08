import random

game = True
options = ['rock', 'paper', 'scissors']
housePoints = 0
userPoints = 0
userInput = ""
houseChoice = ""

while(game):
    choice = False
    print("The score is ",userPoints,"-",housePoints)
    while(choice != True):
        userInput = input("Rock, Paper, or Scissors? ")
        userInput = userInput.lower()
        if(userInput in options):
            choice = True
        else:
            print("Please type in a valid option")
    houseChoice = random.choice(options)
    print("The house chose : ",houseChoice)
    if(houseChoice == userInput):
        print("\nIt's a tie!")
    elif(userInput == "paper"):
        if(houseChoice == "rock"):
            print("You won!")
            userPoints += 1
        else:
            print("You lost!")
            housePoints += 1
    elif(userInput == "rock"):
        if(houseChoice == "scissors"):
            print("You won!")
            userPoints += 1
        else:
            print("You lost!")
            housePoints +=1
    elif(userInput == "scissors"):
        if(houseChoice == "paper"):
            print("You won!")
            userPoints += 1
        else:
            print("You lost!")
            housePoints +=1
    print("----------------------------------")
    if(housePoints == 3 or userPoints == 3):
        game = False
        break

if(userPoints == 3):
    print("Congratulations, you won the game!")
else:
    print("Defeat, the House won")