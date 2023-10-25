import random

def main():
    fail = 0
    score = 0
    task = []
    level = get_level()
    for questions in range(4):
        x = get_randint(level)
        y = get_randint(level)
        z = f"{x} + {y} = "
        result = x + y
        task.append((z, result))
    for z, result in task:
        while True:
            answer = input(z)
            try:
                answer = int(answer)
            except ValueError:
                fail +=1
                print("EEE")
            if answer != result:
                fail +=1
                print("EEE")
                if fail == 3:
                    print(result)
            if answer == result:
                score += 1
                break
    print(f"Final score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                continue
        except:
            pass

def get_randint(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)

if __name__ == "__main__":
     main()
