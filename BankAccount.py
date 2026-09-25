class BankAccount:
    bank_title = "Nik and Rushil's Royal Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.__account_number = account_number # private
        self._routing_number = routing_number #protected

    @property
    def routing_number(self):
        return self._routing_number
        
    @property
    def account_number(self):
        return self.__account_number

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("You cannot withdraw more than you have")
            return

        self.current_balance -= amount

    def print_customer_information(self):
        print("Bank: "+BankAccount.bank_title)
        print("Customer Name: " + self.customer_name)
        print(f"Account Number: {self.__account_number}")
        print(f"Routing Number: {self._routing_number}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")
