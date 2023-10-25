import csv
name = input("what is your name? ")
house = input("what is your house? ")

with open("names.txt", "a") as file:
    result = csv.DictWriter(file, fieldnames=["name", "house"])
    result.writerow({"name":name, "house":house})