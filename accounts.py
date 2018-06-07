class Account:
    """ Simple account class with balance """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount

    def show_balance(self):
        print("Balance is {}".format(self.balance))


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()
    tim.deposit(1000)
    tim.show_balance()
    tim.withdraw(500)
    tim.show_balance()