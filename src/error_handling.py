class InsufficientFundsError(Exception):
    """Exception raised when attempting to withdraw or transfer more funds than available."""
    def __init__(self, message="Insufficient funds available."):
        self.message = message
        super().__init__(self.message)

class NegativeAmountError(Exception):
    """Exception raised when a negative amount is used in a transaction."""
    def __init__(self, message="Amount must be positive."):
        self.message = message
        super().__init__(self.message)

class BankAccount:
    """A simple BankAccount class with error handling for various operations."""

    def __init__(self, account_number: str, balance: float = 0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Deposit money into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            NegativeAmountError: If the amount is negative.
        """
        if amount < 0:
            raise NegativeAmountError("Cannot deposit a negative amount.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            InsufficientFundsError: If there are not enough funds in the account.
            NegativeAmountError: If the amount is negative.
        """
        if amount < 0:
            raise NegativeAmountError("Cannot withdraw a negative amount.")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds to complete the withdrawal.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount') -> None:
        """Transfer money to another account.

        Args:
            amount (float): The amount to transfer.
            target_account (BankAccount): The account to transfer money to.

        Raises:
            InsufficientFundsError: If there are not enough funds in the account.
            NegativeAmountError: If the amount is negative.
        """
        if amount < 0:
            raise NegativeAmountError("Cannot transfer a negative amount.")
        self.withdraw(amount)
        target_account.deposit(amount)

    def get_balance(self) -> float:
        """Get the current balance of the account.

        Returns:
            float: The current balance.
        """
        return self.balance

def main() -> None:
    """Main function to demonstrate the use of the BankAccount class with error handling."""
    account1 = BankAccount("123456", 500)
    account2 = BankAccount("654321", 300)

    try:
        account1.deposit(200)
        print(f"Account 1 balance after deposit: {account1.get_balance()}")

        account1.withdraw(100)
        print(f"Account 1 balance after withdrawal: {account1.get_balance()}")

        account1.transfer(700, account2)
        print(f"Account 1 balance after transfer: {account1.get_balance()}")
        print(f"Account 2 balance after transfer: {account2.get_balance()}")

    except (InsufficientFundsError, NegativeAmountError) as e:
        print(f"Transaction failed: {e}")

if __name__ == "__main__":
    main()
