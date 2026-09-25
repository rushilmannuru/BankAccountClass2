from BankAccount import BankAccount
from SavingsAccount import Savings
from CheckingAccount import Checking


def main():
    # Scenario
    checking = BankAccount("Juice", 500, 100, "CHECK001", "111000111")
    checking2 = Checking("Leo", 800, 150, "CHECK002", "111000111", 100)
    checking.print_customer_information()

    # Deposit $300 into checking
    checking.deposit(300)
    print(checking.current_balance)

    # Withdraw $200 from checking
    checking.withdraw(200)
    print(checking.current_balance)

    # Try to withdraw $5000 from checking (rejected)
    checking.withdraw(5000)
    print(checking.current_balance)

    savings = Savings("Juice", 1000, 200, "SAVING001", "111000111", 0.05)
    savings2 = Savings("Leo", 1500, 300, "SAVING002", "111000111", 0.05)
    savings.print_customer_information()

    # Deposit $500 into savings
    savings.deposit(500)
    print(savings.current_balance)

    # Add 5% interest to savings
    savings.add_interest()
    print(savings.current_balance)

    # Withdraw $300 from savings
    savings.withdraw(300)
    print(savings.current_balance)

    # Print second checking
    checking2.print_customer_information()

    # Deposit $500
    checking2.deposit(500)
    print(checking2.current_balance)

    # Transfer $50
    checking2.transfer(50)
    print(checking2.current_balance)

    savings2.print_customer_information()
    savings2.deposit(500)
    print(savings2.current_balance)


if __name__ == "__main__":
    main()
