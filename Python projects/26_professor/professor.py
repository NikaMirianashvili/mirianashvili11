import random


    
def main():
    n = get_level()
    i=10
    while i>0:
        i-=1
        x = generate_integer(n)
        y = generate_integer(n)
        solution = generate_equation_solution(x, y)
        j=3
        while j>0:
            j-=1
            try:
                print(x, "+", y, "= ", end="")
                if check_user_input(solution):
                    break
                elif j==0:
                    print("EEE")
                    print(x, "+", y, "= ", solution)
                else:
                    print("EEE")
            except ValueError:
                pass

def get_level():
    while True:
            try:
                user_input = int(input("Level: "))
                if user_input == 1 or user_input == 2 or user_input == 3 :
                    break
            except ValueError:
                    pass
            else:
                continue
    return user_input

    
def generate_integer(level):
    numberList =[]
    if level == 1:
        numberList = range(1, 10)
    elif level == 2:
        numberList = range(10, 100)
    elif level == 3:
        numberList = range(100, 1000)

    number = random.choice(numberList)
    return number

   
def generate_equation_solution(num1, num2):
    sum = num1+num2
    return sum

def check_user_input(solution):
     userInput = int(input())
     if userInput == solution:
        return True

if __name__ == "__main__":
    main()
