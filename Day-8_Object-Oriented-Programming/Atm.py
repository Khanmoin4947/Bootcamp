class ATM:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def transfer(self, receiver, amount):
        self.balance -= amount
        receiver.balance += amount
        print(f"₹{amount} transferred from {self.name} to {receiver.name}")
        
    def show_balance(self):
        print(f"{self.name}'s Balance: ₹{self.balance}")


a1 = ATM("Moin", 5000)
a2 = ATM("Navjot", 2000)

a1.show_balance()
a2.show_balance()

a1.transfer(a2, 1500)

a1.show_balance()
a2.show_balance()