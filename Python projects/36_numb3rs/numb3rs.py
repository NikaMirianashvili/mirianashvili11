import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    if matches:
            first = matches.group(1)
            second = matches.group(2)
            third = matches.group(3)
            fourth = matches.group(4)
            if int(first)<=255 and int(second)<=255 and int(third)<=255 and int(fourth)<=255:
                return True
            else: 
                return False
    else:
         return False

if __name__ == "__main__":
    main()
