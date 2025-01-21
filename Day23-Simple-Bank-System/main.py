from utils.bank import Bank
from utils.bankAccount import BankAccount

user_menu = """Enter:
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transfer
6. Quit
Your Choice: """

def prompt_create_account(bank):
    account_type = input('Enter account type: ')
    account_holder = input('Enter account holder name: ')
    try:
        initial_deposit = float(input('Enter initial deposit: '))
        account = BankAccount(account_type, account_holder, initial_deposit)
        bank.create_account(account)
        print(f"Account created successfully! ")
        print(f"Your account is {account.account_number}")
    except ValueError as e:
        print(f"Error: {e}")

def prompt_deposit(bank):
    try:
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        bank.find_account(account_number).deposit(amount)
        print("Deposit successful!")
    except ValueError as e:
        print(f"Error: {e}")

def prompt_withdraw(bank):
    try:
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        bank.find_account(account_number).withdraw(amount)
        print("Withdrawal successful!")
    except ValueError as e:
        print(f"Error: {e}")


def prompt_check_balance(bank):
    try:
            account_number = int(input("Enter account number: "))
            account = bank.find_account(account_number)
            print(f"Balance: ${account.balance:.2f}")
           
    except ValueError as e:
            print(f"Error: {e}")

def prmpot_transer_amount(bank):
    try:
            from_account = int(input("From account number: "))
            to_account = int(input("To account number: "))
            amount = float(input("Amount to transfer: "))
            bank.transfer(from_account, to_account, amount)
    except ValueError as e:
            print(f"Error: {e}")


def main():
    bank = Bank()
    while True:

        user_choice = input(user_menu).strip()

        if user_choice == "1":
            prompt_create_account(bank)

        elif user_choice == "2":
            prompt_deposit(bank)

        elif user_choice == "3":
            prompt_withdraw(bank)

        elif user_choice == "4":
           prompt_check_balance(bank)
                
        elif user_choice == "5":
             prmpot_transer_amount(bank)
            
        elif user_choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
