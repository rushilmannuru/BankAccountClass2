from BankAccount import BankAccount

class Savings(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_number)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.current_balance += self.current_balance * self.interest_rate

    def print_customer_information(self):
        super().print_customer_information()
        print(self.interest_rate)
