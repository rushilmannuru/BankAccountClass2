class BankAccount:
    bank_title = "My Royal Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("You cannot withdraw more than you have")
            return

        self.current_balance -= amount

    def print_customer_information(self):
        print(self.bank_title)
        print(self.customer_name)
        print(self.current_balance)
        print(self.minimum_balance)

acct1 = BankAccount("Nikolas Yanez", 1000, 100)
acct1.deposit(100)
acct1.withdraw(1200)
acct1.print_customer_information()

acct2 = BankAccount("Spider-Man", 200, 50)
acct2.deposit(1000)
acct2.withdraw(200)
acct2.print_customer_information()