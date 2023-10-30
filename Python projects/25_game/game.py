import random


def main():

    n = int(input("write a level : "))
    myList = range(1, n)
    guessingNumber = random.choice(myList)
    while True:
        try:
            userInput = int(input("Guess: "))
            if userInput > guessingNumber:
                print("Too Large!")
                continue
            elif userInput < guessingNumber:
                print("Too Little!")
                continue
            else:
                print("Just right! ")
                break
        except ValueError:
            pass
        else:
            break
main()
