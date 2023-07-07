import unittest

from .account import Account

class TestAccount(unittest.TestCase):
    def test_increment_balance_above_limit(self):
        """
        Test that it increments the balance if the new amount is less than the limit
        """
        account = Account('4111111111111111', 0)

        account.increment_balance(1)

        self.assertEqual(account.balance, 0)

    def test_increment_balance_above_limit(self):
        """
        Test that it increments the balance if the new amount is less than the limit
        """
        account = Account('4111111111111111', 10)

        account.increment_balance(1)

        self.assertEqual(account.balance, 1)

    def test_increment_balance_above_limit(self):
        """
        Test that it not increments the balance if the new amount is greater than limit
        """
        account = Account('4111111111111111', 1)

        account.increment_balance(10)

        self.assertEqual(account.balance, 0)

    def test_decrement_balance_without_limit(self):
        """
        Test that it decrements the balance even the limit is zero
        """
        account = Account('4111111111111111', 0)

        account.decrement_balance(1)

        self.assertEqual(account.balance, -1)

    def test_decrement_balance(self):
        """
        Test that it decrements the balance
        """
        account = Account('4111111111111111', 10)
        account.balance = 5

        account.decrement_balance(5)

        self.assertEqual(account.balance, 0)

    def test_decrement_balance_negative(self):
        """
        Test that it decrements the balance and the balance is negative
        """
        account = Account('4111111111111111', 0)
        account.balance = 0

        account.decrement_balance(10)

        self.assertEqual(account.balance, -10)

    def test_invalid_number_card(self):
        """
        Test that it detect the error in the number card
        """
        account = Account('1234567890123456', 0)
        self.assertEqual(len(account.errors), 1)

    def test_decrement_balance_without_limit(self):
        """
        Test that it decrements the balance even the limit is zero
        """
        account = Account('1234567890123456', 0)

        account.decrement_balance(1)

        self.assertEqual(account.balance, 0)

    def test_decrement_balance(self):
        """
        Test that it decrements the balance
        """
        account = Account('1234567890123456', 0)
        account.balance = 5

        account.decrement_balance(5)

        self.assertEqual(account.balance, 5)

    def test_decrement_balance_negative(self):
        """
        Test that it decrements the balance and the balance is negative
        """
        account = Account('1234567890123456', 0)
        account.balance = 0

        account.decrement_balance(10)

        self.assertEqual(account.balance, 0)

if __name__ == '__main__':
    unittest.main()
