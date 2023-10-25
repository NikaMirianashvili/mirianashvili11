import random

def main():
    level = get_level()
    score = 0
    fail = 0
    task = []
    for question in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = f"{x} + {y} = "
        result = x + y
        task.append((z, result))
    for z, result in task:

        while True:
            answer = input(z)
            try:
                answer = int(answer)
            except ValueError:
                fail += 1
                print ("EEE")
            if answer != result:
                fail += 1
                print("EEE")
                if fail == 3:
                    print (result)
                    break
            if answer == result:
                score += 1
                break


    print(f"Score: {score}")

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


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()