from BankAccount import BankAccount

class Checking(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number)
        self.transfer_limit = transfer_limit
        self.transfer_count = 0

    def transfer(self, amount):
        if self.transfer_count >= self.transfer_limit:
            print("You have reached the transfer limit")
            return
        if self.current_balance - amount < self.minimum_balance:
            print("You cannot transfer more than you have.")
            return

        self.transfer_count += 1
        self.current_balance -= amount
