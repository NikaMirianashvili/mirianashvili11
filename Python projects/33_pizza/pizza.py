import sys
import csv
from tabulate import tabulate

try:
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
    else: 
        with open(sys.argv[1]) as file:
            table = []
            headers = []
            i=0
            cvsFile = csv.reader(file)
            for row in cvsFile:
                if i==0: 
                     headers = row
                     i+=1
                else:
                    table.append(row)
        print(headers)
        print(tabulate(table, headers, tablefmt="grid"))
       
      
except FileNotFoundError:
    sys.exit("File does not exist")