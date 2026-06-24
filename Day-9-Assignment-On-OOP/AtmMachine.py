class ATM:
    def __init__(self, pin, balance, owner):
        self.__pin = pin
        self.__balance = balance
        self._owner = owner
        self.__authenticated = False

    def authenticate(self, pin):
        if pin == self.__pin:
            self.__authenticated = True
            print("Authentication Successful")
        else:
            print("Wrong PIN")

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amt):
        if not self.__authenticated:
            print("Please authenticate first")
            return

        self.__balance += amt
        print("Deposited:", amt)

    def withdraw(self, amt):
        if not self.__authenticated:
            print("Please authenticate first")
            return

        if amt > 20000:
            raise ValueError("Maximum withdrawal limit is ₹20,000")

        if amt > self.__balance:
            raise ValueError("Insufficient Balance")

        self.__balance -= amt
        print("Withdrawn:", amt)

    def mini_statement(self):
        print("Owner:", self._owner)
        print("Balance:", self.__balance)


# Example
atm = ATM(1234, 50000, "Moin")

atm.authenticate(1234)
atm.deposit(5000)
atm.withdraw(10000)

atm.mini_statement()

print("Current Balance:", atm.balance)