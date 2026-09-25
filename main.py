from BankAccount import BankAccount
from SavingsAccount import Savings


def main():
    # Scenario
    checking = BankAccount("Alice", 500, 100, "CHECK001")
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

    savings = Savings("Alice", 1000, 200, "SAVING001", 0.05)
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


if __name__ == "__main__":
    main()
