import sys
import os
import unittest

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from error_handling import BankAccount, InsufficientFundsError, NegativeAmountError

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account1 = BankAccount("123456", 500)
        self.account2 = BankAccount("654321", 300)

    def test_deposit(self):
        self.account1.deposit(200)
        self.assertEqual(self.account1.get_balance(), 700)
        with self.assertRaises(NegativeAmountError):
            self.account1.deposit(-50)

    def test_withdraw(self):
        self.account1.withdraw(100)
        self.assertEqual(self.account1.get_balance(), 400)
        with self.assertRaises(InsufficientFundsError):
            self.account1.withdraw(1000)
        with self.assertRaises(NegativeAmountError):
            self.account1.withdraw(-50)

    def test_transfer(self):
        self.account1.transfer(200, self.account2)
        self.assertEqual(self.account1.get_balance(), 300)
        self.assertEqual(self.account2.get_balance(), 500)
        with self.assertRaises(InsufficientFundsError):
            self.account1.transfer(1000, self.account2)
        with self.assertRaises(NegativeAmountError):
            self.account1.transfer(-50, self.account2)

    def test_get_balance(self):
        self.assertEqual(self.account1.get_balance(), 500)
        self.assertEqual(self.account2.get_balance(), 300)

if __name__ == "__main__":
    unittest.main()
