def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>=2 and len(s)<=6:
        if len(s)== 2:
            if s.isalpha():
                return True
        
        elif len(s)== 3:
            if s[0].isalpha() and s[1].isalpha():
                if s[2].isalpha():
                    return True
                elif s[2].isdigit() and int(s[2]) != 0:
                        return True
                else: False
            else: False
        
        elif len(s)== 4:
            if s[0].isalpha() and s[1].isalpha():
                if s[2].isalpha() and s[3].isalpha():
                    return True
                elif s[2].isalpha() and s[3].isdigit() and int(s[3]) != 0:
                        return True
                elif s[2].isdigit() and s[3].isdigit() and int(s[2]) != 0:
                        return True
                else: False
            else: False
        
        elif len(s)== 5:
            if s[0].isalpha() and s[1].isalpha():
                if s[2].isalpha() and s[3].isalpha() and s[4].isalpha():
                    return True
                elif s[2].isalpha() and s[3].isalpha() and s[4].isdigit() and int(s[4]) != 0:
                        return True
                elif s[2].isalpha() and s[3].isdigit() and s[4].isdigit() and int(s[3]) != 0:
                        return True
                elif s[2].isdigit() and s[3].isdigit() and s[4].isdigit() and int(s[2]) != 0:
                        return True
                else: False
            else: False
        
        elif len(s)== 6:
            if s[0].isalpha() and s[1].isalpha():
                if s[2].isalpha() and s[3].isalpha() and s[4].isalpha() and s[5].isalpha():
                    return True
                elif s[2].isalpha() and s[3].isalpha() and s[4].isalpha() and s[5].isdigit() and int(s[5]) != 0:
                        return True
                elif s[2].isalpha() and s[3].isalpha() and s[4].isdigit() and s[5].isdigit() and int(s[4]) != 0:
                        return True
                elif s[2].isalpha() and s[3].isdigit() and s[4].isdigit() and s[5].isdigit() and int(s[3]) != 0:
                        return True
                elif s[2].isdigit() and s[3].isdigit() and s[4].isdigit() and s[5].isdigit() and int(s[2]) != 0:
                        return True
                else: False
            else: False
        else:
                False


if __name__ == "__main__":
    main()