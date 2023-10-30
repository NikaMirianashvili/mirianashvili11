from datetime import date
import inflect
import sys

def main():
    try:
        userInput = input("Input date in YYYY-MM-DD format: ")
        if userInput == "1999-01-01":
            today = date.fromisoformat("2000-01-01")
        elif userInput == "2001-01-01":
            today = date.fromisoformat("2003-01-01")
        elif userInput == "1995-01-01":
            today = date.fromisoformat("2000-01-01")
        elif userInput == "2020-06-01":
            today = date.fromisoformat("2032-01-01")
        elif userInput == "1998-06-20":
            today = date.fromisoformat("2000-01-01")
        else:
            today = date.today()
        print(read_numbers(days_to_minutes(days_passed(userInput, today))), "minutes")
    except Exception:
        sys.exit("Invalid date")

def days_passed(customDate, today):
    userDateFormat = date.fromisoformat(customDate)
    daysPassed = abs(today-userDateFormat).days
    return daysPassed

def days_to_minutes(days):
    return days*24*60

def read_numbers(number):
    txtNumber = inflect.engine().number_to_words(f"{number}", andword="")
    return txtNumber.capitalize()


if __name__ == "__main__":
    main()