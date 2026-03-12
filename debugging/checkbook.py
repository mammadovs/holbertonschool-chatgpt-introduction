class Checkbook:
    """
    A simple checkbook class to manage deposits, withdrawals, and balance inquiries.

    Attributes:
        balance (float): The current balance of the checkbook.
    """

    def __init__(self):
        """Initialize the checkbook with a balance of 0.0."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a given amount into the checkbook.

        Parameters:
            amount (float): The amount to deposit. Must be positive.

        Raises:
            ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraw a given amount from the checkbook.

        Parameters:
            amount (float): The amount to withdraw. Must be positive and not exceed the balance.

        Raises:
            ValueError: If the amount is not positive.
            RuntimeError: If insufficient funds are available.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise RuntimeError("Insufficient funds to complete the withdrawal.")
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        """Print the current balance of the checkbook."""
        print(f"Current Balance: ${self.balance:.2f}")


def get_valid_amount(prompt):
    """
    Prompt the user for a numeric amount and validate the input.

    Parameters:
        prompt (str): The input prompt for the user.

    Returns:
        float: A valid positive numeric amount.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Amount must be positive. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    """Main loop to interact with the user for deposit, withdraw, and balance operations."""
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Exiting program. Goodbye!")
            break
        elif action == 'deposit':
            amount = get_valid_amount("Enter the amount to deposit: $")
            try:
                cb.deposit(amount)
            except ValueError as e:
                print(e)
        elif action == 'withdraw':
            amount = get_valid_amount("Enter the amount to withdraw: $")
            try:
                cb.withdraw(amount)
            except (ValueError, RuntimeError) as e:
                print(e)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
