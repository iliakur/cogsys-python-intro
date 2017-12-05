class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)


class BlockedAccount(MinimumBalanceAccount):
    """Shitty student account"""
    def __init__(self, starting_balance):
        super().__init__(0)

        min_amount = 9000
        if starting_balance < min_amount:
            raise ValueError("Need at least {}".format(min_amount))
        self.balance = starting_balance
        self.monthly_outgoing = 0

    def withdraw(self, amount):
        if amount + self.monthly_outgoing > 700:
            raise ValueError("Exceeded monthly withdrawal limit")
        super().withdraw(amount)
