import sys
import csv


try:
    if len(sys.argv) != 3:
        if len(sys.argv)<3:
            sys.exit("Too few arguments")
        else:
            sys.exit("Too many arguments")
    else:
        with open(sys.argv[1]) as before_file:
            before_data = csv.DictReader(before_file)

            for row in before_data:
                fullName, house = row['name'], row['house']
                name, surname = fullName.strip().split(",")
                name = name.strip()
                surname = surname.strip()
                
                with open(sys.argv[2], 'a', newline='') as after_file:
                    writer = csv.DictWriter(after_file, fieldnames=['name', 'surname', 'house'])
                    writer.writeheader()
                    writer.writerow({'name': name, 'surname': surname, 'house': house})
        
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")