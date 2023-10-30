from validator_collection import checkers

def main():
    print(validate_email(input("What's your email address? ").strip()))


def validate_email(e):
    if checkers.is_email(e):
        return "Valid"
    else:
        return "Invalid"
if __name__ == "__main__":
    main()