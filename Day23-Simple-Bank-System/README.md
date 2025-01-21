Bank Account Management System

Overview

This project is part of Day 23 of my 100-Day Python Code Challenge. The goal of this project is to build a simple Bank Account Management System that supports operations like creating accounts, depositing, withdrawing, transferring funds, and checking balances. The project also includes unit tests to ensure code quality and functionality.

Features

1. BankAccount Class

Represents individual bank accounts.

Attributes:

account_type: Type of the account (e.g., Savings, Checking).

account_number: A unique account number generated automatically.

account_holder: Name of the account holder.

balance: Current balance in the account.

Methods:

deposit(amount): Adds funds to the account.

withdraw(amount): Withdraws funds from the account.

get_balance: Retrieves the current balance along with the account number.

2. Bank Class

Manages multiple bank accounts.

Features:

create_account(account): Adds a new account to the system.

delete_account(account_number): Deletes an account by its account number.

find_account(account_number): Retrieves an account object by its account number.

transfer(from_account_number, to_account_number, amount): Transfers funds between two accounts.

is_account_valid(account_number): Validates the existence of an account.

3. Command-Line Interface

Allows users to interact with the system using a menu.

Actions include:

Creating a new account.

Depositing funds.

Withdrawing funds.

Checking balance.

Transferring funds.

Unit Testing

The project includes unit tests to validate the functionality of the Bank and BankAccount classes.

Tests include:

Validating deposits and withdrawals.

Checking for invalid operations (e.g., negative deposits, overdrafts).

Ensuring account creation and deletion work as expected.

Verifying transfer functionality.

Framework: unittest

Key Learnings

Practiced writing unit tests with the unittest framework.

Improved understanding of object-oriented programming concepts in Python.

Learned how to handle edge cases and validate user inputs effectively.

Gained experience in modular project organization.