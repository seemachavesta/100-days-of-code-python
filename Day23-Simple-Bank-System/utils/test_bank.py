import unittest
from bank import Bank
from bankAccount import BankAccount

class TestBank(unittest.TestCase):
    def test_create_account_invalid_account(self):
        bank = Bank()
        with self.assertRaises(ValueError):
            bank.create_account(None)

        account = object()
        with self.assertRaises(ValueError):
            bank.create_account(account)

    
    
    def test_delete_account(self):
        bank = Bank()
        account = BankAccount('Savings', 'Miller Rock', 100)
       
        bank.create_account(account)
        
        try:
            bank.is_account_valid(1000000000)
        except ValueError:
            self.fail('Account should be valid before deletion')
        

        bank.delete_account(1000000000)

        with self.assertRaises(ValueError):
            bank.is_account_valid(1000000000)

        with self.assertRaises(ValueError):
            bank.is_account_valid(99999999)
        
        




if __name__ == "__main__":
    unittest.main()