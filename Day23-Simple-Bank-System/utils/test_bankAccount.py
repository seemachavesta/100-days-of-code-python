import unittest
from bankAccount import BankAccount
from bank import Bank

class TestBankAccount(unittest.TestCase):
    def test_depost(self):
        account = BankAccount("Savings", "John Doe", 100.0)
        account.deposit(50)

        self.assertEqual(account.balance, 150)


    def test_deposit_invalid_amount(self):
        account = BankAccount('Savings', 'Miller Rock', 100)
        with self.assertRaises(ValueError):
            account.deposit(-10.00)

        with self.assertRaises(ValueError):
            account.deposit(-5)

        with self.assertRaises(ValueError):
            account.deposit(0)

        with self.assertRaises(TypeError):
            account.deposit('hello')

    def test_withdraw(self):
        account = BankAccount('Savings', 'Miller Rock', 100)
        account.withdraw(50)
        self.assertEqual(account.balance, 50)

    def test_invalid_withdraw_amount(self):
        account = BankAccount('Savings', 'Miller Rock', 100)
        
        with self.assertRaises(ValueError):
            account.withdraw(101)

        with self.assertRaises(ValueError):
            account.withdraw(-10)

        with self.assertRaises(ValueError):
            account.withdraw(0)

        with self.assertRaises(TypeError):
            account.withdraw('Hello')
        

  






if __name__ == "__main__":
    unittest.main()

        

    
