class account():
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    def deposit(self, n):
        self._balance += n
    def withdraw(self, n):
        self._balance -= n

def main():
    Account = account()
    print("Balance: ", Account.balance)
    Account.deposit(100)
    Account.withdraw(50)
    print("Balance: ", Account.balance)

main()