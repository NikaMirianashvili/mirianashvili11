import sys
try:
    if len(sys.argv) == 1: 
        print("Too few command - line arguments")
    elif len(sys.argv) > 2:
        print("Too many command - line arguments")
    else: 
        with open(sys.argv[1]) as file:
            count = 0
            for line in file:
                line = line.strip()
                if line.strip() == '':
                    pass
                elif line.strip()[0] != "#":
                    count +=1 

        print("total lines", count)
except FileNotFoundError:
    print("File doesn't exist")