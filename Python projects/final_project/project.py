import random
import re
from enum import IntEnum
    
#this class makes code easier to read
class Shoot(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

User_Score_Count = 0
Computer_Score_Count = 0
#if user writes something other than given 3 actions, they will be notified to fix it.
#after first game user will be asked if they want to keep playing or quit
#loop will be over if user press any other character than Y
def main():
    while True:
        try:
            userInputEncrypted = user_input_encrypt(input("Rock, Paper, Scissors, Lizard or Spock?: "))
            computerInput = computer_input()
            match_shoots_output(userInputEncrypted, computerInput)
        except TypeError:
            pass
        else:
            result = match_result(userInputEncrypted, computerInput)
            print(result)
            print(f"User vs Computer - {User_Score_Count}:{Computer_Score_Count}")
            question = input("If you want to keep playing type Y. (To quit type any other character) ")
            if re.match("^[Y]{1}$", question, re.IGNORECASE):
                continue
            else:
                break

# fanction changes user input into numbers which now are called using Shoot class
# rock is 0, same as Shoot.Rock
# paper is 1 same as Shoot.Paper
# scissors is 2 same as Shoot.Scissors
# lizard is 3 same as Shoot.Lizard
# spock is 4 same as Shoot.Spock

def user_input_encrypt(userInput):
    if userInput.lower() == "rock":
        return Shoot.Rock
    elif userInput.lower() == "paper":
        return Shoot.Paper
    elif userInput.lower() == "scissors":
        return Shoot.Scissors
    elif userInput.lower() == "lizard":
        return Shoot.Lizard
    elif userInput.lower() == "spock":
        return Shoot.Spock
    else:
        print("Please write one of the five possible actions")
        
        
# computer's action is chosen randomly from list [0, 1, 2]
def computer_input():
    return random.choice(range(len(Shoot)))


def index_to_text(index):
    shoots = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    return shoots[index]

def match_shoots_output(user_input, computer_input):
    #user's choice output on screen
    print("User played:", index_to_text(user_input))
    #computer's choice output on screen
    print("Computer played:", index_to_text(computer_input))

def match_result(user_input, computer_input):
    winning = {
        Shoot.Rock: [Shoot.Scissors, Shoot.Lizard], #rock beats scissors and lizard
        Shoot.Paper: [Shoot.Rock, Shoot.Spock],    #paper beats rock and spock
        Shoot.Scissors: [Shoot.Paper, Shoot.Lizard], #scissors beats paper and lizard
        Shoot.Lizard: [Shoot.Paper, Shoot.Spock], #Lizard beats paper and spock
        Shoot.Spock: [Shoot.Rock, Shoot.Scissors], #Spock beats Rock and Scissors
    }
    user_win = winning[user_input]
    if user_input == computer_input:
        return "It's a tie"
    elif computer_input in user_win:
        increment_user_score()
        return f"You Won!, {index_to_text(user_input)} beats {index_to_text(computer_input)}"
    else:
        increment_computer_score()
        return f"You Lost, {index_to_text(computer_input)} beats {index_to_text(user_input)}"

def increment_user_score():
    global User_Score_Count
    User_Score_Count += 1

def increment_computer_score():
    global Computer_Score_Count
    Computer_Score_Count += 1

if __name__ == "__main__":
    main()