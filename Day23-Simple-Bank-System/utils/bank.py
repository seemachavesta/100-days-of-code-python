
class Bank:
    def __init__(self):
        self.accounts = {}
        
    def __repr__(self):
        return "\n".join([str(account) for account in self.accounts.values()])
    
    # Function to check if account numbe exists 
    def is_account_valid(self, account_number: int):
        if account_number not in self.accounts:
            raise ValueError(f"Account Number {account_number} is not found")

     # Create new bank account   
    def create_account(self, account):
       
        if not account or not hasattr(account, 'account_number'):
            raise ValueError("Invalid account object provided.")
            
        if account.account_number in self.accounts:
            raise ValueError("Account with this number already exists.")
            
        self.accounts[account.account_number] = account
     
       
    def delete_account(self, account_number: int):
        """Function to delete account using the account number"""
        self.is_account_valid(account_number)  
        del self.accounts[account_number]

    
    def find_account(self, account_number):
        self.is_account_valid(account_number)  
        #Return the account object
        return self.accounts[account_number]
        
    
    def transfer(self, from_account_number: int, to_account_number: int, amount: float):
        """Transfer amount from one account another account using the account number"""    
        self.is_account_valid(from_account_number)
        self.is_account_valid(to_account_number)

            
        from_account = self.accounts[from_account_number]
        to_account = self.accounts[to_account_number]
        if from_account.balance < amount:
            raise ValueError("Account can't be transfer due to insificiant funds")
            
        from_account.withdraw(amount)
        to_account.deposit(amount)
        
        print(f"Successfully transferred ${amount:.2f} from {from_account_number} to {to_account_number}.")


    def check_balance(self, account_number):
        self.is_account_valid(account_number)
        
        result = self.accounts[account_number]
        print(result)


