# Regular method, classmethods and staticmethods


class BankAccount:

    bank_name = "Somali Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Instance method
    def deposit(self, amount):
        self.balance += amount

    # Class method
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    # Static method
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0


acc_1 = BankAccount('Ahmed', 1000)
acc_1.deposit(100)

print(acc_1.balance)