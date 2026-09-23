
class BankAccount:
    bank_title="Chase Bank"
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount

    def print_customer_information(self):
        print("Bank:"+BankAccount.bank_title)
        print("Customer Name: " + self.customer_name)
        print(f"Current Balance:   {self.current_balance}")
        print(f"Minimum Balance:  {self.minimum_balance}")


instance1 = BankAccount("Rushil", 1000, 100)
instance1.deposit(100)
instance1.withdraw(1200)
instance1.print_customer_information()

instance2 = BankAccount("Akhi", 200, 100)
instance2.deposit(2500)
instance2.withdraw(500)
instance2.print_customer_information()