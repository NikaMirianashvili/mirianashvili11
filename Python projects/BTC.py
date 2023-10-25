def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    while True:
        # max and min charakter
        if len(s) < 2 or len(s) > 6:
            return False

        # start with two letter
        if s[0:2].isdigit():
            return False

        # numbers in middle
        for char in s:
            if char.isdigit():
                index = s.index(char)
                if not s[index:].isdigit():
                    return False

        # first number cannot be 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                if s[i] == "0":
                    return False
                break
            i += 1


        # no periods, space...
        not_allowd = (" ", ".", ",", "!", "?", ";", ":")
        for char in s:
            if char in not_allowd:
                return False

        return True

if __name__ == "__main__":
    main()







