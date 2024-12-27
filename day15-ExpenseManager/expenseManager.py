from expense import Expense

class ExpenseManager:
    def __init__(self, file_name='expenses.csv'):
        self.file_name = file_name
   
    # Read the csv file 
    def file_reader(self, file_name):
        with open(file_name, 'r') as expense_file:
            return [file.strip() for file in expense_file]
    
    # Add expneses in csv file 
    def add_expense(self, expense):
        #Try to read the file if exists
        try:
            existing_expenses = self.file_reader(self.file_name)
        except FileNotFoundError:
            existing_expenses = []

        if expense.to_string().strip() in existing_expenses:
            print('Expense already exists')
            return
        # Append the expenses in file 
        with open(self.file_name, 'a') as expense_file:
            expense_file.write(expense.to_string() + '\n')
            print(f"Expense added: {expense.to_string()}")

   # Display expenses 
    def view_expenses(self):
        try:
            expense_list = self.file_reader(self.file_name)
        except FileNotFoundError:
            print('File does not exist')
            return

        for expense in expense_list:
            try:
                category, description, amount, date = expense.split(',')
                print(f'Category: {category}, Description: {description}, Amount: {amount}, Date: {date}')
                print('-' * 40)
            except ValueError:
                print(f"Malformed line in file: {expense}")
    
    # Delete expesnses from file using categories  
    def delete_expense(self, category):
        try:
            expenses = self.file_reader(self.file_name)
        except FileNotFoundError:
            print('File not found')
            return

        updated_expenses = [
            expense.strip() for expense in expenses if not expense.lower().startswith(category.lower())
        ]

        if not updated_expenses:
            print(f"No expenses found for category: {category}")
        else:
            with open(self.file_name, 'w') as file:
                file.write('\n'.join(updated_expenses) + '\n')
            print(f"Deleted all expenses in category: {category}")

    #Search expenses by category from csv file
    def search_expenses_by_category(self, category):
        try:
            expenses = self.file_reader(self.file_name)
        except FileNotFoundError:
            print('File does not exist')
            return

        filtered_expenses = [
            expense for expense in expenses if expense.lower().startswith(category.lower())
        ]

        if not filtered_expenses:
            print(f"No expenses found for category: {category}")
        else:
            for line in filtered_expenses:
                try:
                    category, description, amount, date = line.split(',')
                    print(f'Category: {category}, Description: {description}, Amount: {amount}, Date: {date}')
                except ValueError:
                    print(f"Malformed line in file: {line}")


# Example usage
expense = Expense('Food', 'Groceries', 50.0, '2024-12-24')
expense1 = Expense('Rent', 'Bills', 1200.0, '2024-12-24')

expense_manager = ExpenseManager()

expense_manager.add_expense(expense)
expense_manager.add_expense(expense1)
expense_manager.view_expenses()

expense_manager.delete_expense('Rent')
expense_manager.view_expenses()