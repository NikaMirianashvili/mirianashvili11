def main():
    total = 50
    print("Amount Due: ", total)
    while total <= 50:
        total = count_due(total)
        if total<0:
            print("Change Owed: ", abs(total))
            break
        print("Amount Due: ", total)



def count_due(n):
    payed = amount_payed()
    due = n - payed
    return due

def amount_payed():
    while True:
        try:
            payed = int(input("Insert Coin: " ))
        except ValueError:
            print("Please input coin in the machine")
        else:
            break

    if payed == 5 or payed == 10 or payed ==25:
        return payed
    else:
        print("Machine only accepts 5, 10, and 25 cents!")
        return 0
#ჰჯჰდსდ
main()