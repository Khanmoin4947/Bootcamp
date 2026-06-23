class Bank:
    def __init__(self, balnc):
        self.balnc = balnc

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError
        self.balnc += amount

    def withdraw(self, amount):
        if amount > self.balnc:
            raise InsufficientFundsError
        self.balnc -= amount

class InsufficientFundsError(Exception):
    pass
class InvalidAmountError(Exception):
    pass

acc_1 = Bank(1000)

try:
    acc_1.deposit(500)
    acc_1.withdraw(200)
    acc_1.withdraw(2000)

except InvalidAmountError:
    print("Invalid amount!")

except InsufficientFundsError:
    print("Not enough balnc!")

print("balnc =", acc_1.balnc)