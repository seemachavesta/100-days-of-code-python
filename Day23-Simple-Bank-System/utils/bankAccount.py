class BankAccount:
    _next_account_number = 1000000000
    def __init__(self, account_type, account_holder, initial_deposit: float):
        self.account_type = account_type 
        self.account_number = BankAccount._next_account_number
        BankAccount._next_account_number += 1
        self.account_holder = account_holder
        self.balance = initial_deposit
        
    def __repr__(self):
        return (f"Account Type: {self.account_type}, "
                f"Account Number: {self.account_number}, "
                f"Account Holder: {self.account_holder}, "
                f"Balance: ${self.balance:.2f}")
                

    def deposit(self, amount: float):
        """Deposits a valid amount into the account balance."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
            
        self.balance += amount
        
            
    def withdraw(self, amount: float):
        """Function to withdraw valid amount from account"""
        if not isinstance(amount, (int, float)):
            raise TypeError('Amount must be a number.')
        
        if amount <= 0:
            raise ValueError("Withdrawal amount amount must be greater than zero")
            
        if amount > self.balance:
            raise ValueError('Insufficient balance for this withdrawal')
           
        self.balance -= amount
        
   
    
    

